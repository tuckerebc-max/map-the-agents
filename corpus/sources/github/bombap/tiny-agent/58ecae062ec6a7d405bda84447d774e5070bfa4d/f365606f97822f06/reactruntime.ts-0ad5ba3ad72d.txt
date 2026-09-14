// Agent runtime

import { UUID } from 'crypto';
import { buildContext, formatMessageHistory, formatProviders } from '../context.ts';
import { LLMEngine } from '../llm-engine.ts';
import { parseJSONBlock } from '../parsing.ts';
import * as Templates from '../templates/index.ts';
import { ITool, State, IAgentRuntime, IProvider, IClient, Message } from '../types.ts';
import { ConsoleLogger } from '../console.ts';

const MAX_STEPS = parseInt(process.env.MAX_STEPS || '20');

export class ReactAgentRuntime implements IAgentRuntime {

    readonly llmEngine: LLMEngine;
    private clients: Map<string, IClient>;
    state: State;
    tools: ITool[];
    providers: IProvider[];
    id: UUID;
    private readonly MESSAGE_BUFFER_SIZE = 33;
    private readonly STEPS_BUFFER_SIZE = 33;
    messageBuffer: Message[];

    constructor(tools: ITool[] = [], providers: IProvider[] = []) {
        ConsoleLogger.info('Initializing Agent');
        this.llmEngine = LLMEngine.getInstance();
        this.state = {};
        this.tools = tools;
        this.providers = providers;
        this.id = crypto.randomUUID();
        this.clients = new Map();
        this.messageBuffer = [];

        ConsoleLogger.success(`Initialized Agent with id: ${this.id}`);
    }

    public async run(state: State): Promise<void> {
        ConsoleLogger.log(`AGENT[${this.id}] Running Agent...`);
        this.updateState(state);
        //ConsoleLogger.debug(`Running Agent with state: ${JSON.stringify(this.state)}`);

        // Add providers
        const providersData = await formatProviders(this.providers);
        this.updateState({ providersData: providersData });

        let stepsCount = 0;
        while (!this.state.completed) {
            stepsCount++;
            ConsoleLogger.log(`AGENT[${this.id}] Running step ${stepsCount}`);
            const response = await this._step();
            if (!response) {
                ConsoleLogger.error('AGENT[${this.id}] No response from LLM');
                throw new Error('No response from LLM');
            }
            if (process.env.SAFE_MODE && stepsCount > MAX_STEPS) {
                ConsoleLogger.warn(`AGENT[${this.id}] Safe mode enabled, stopping execution`);
                break;
            }
        }

        if (!this.state.finalAnswer) {
            ConsoleLogger.error('No final answer');
            throw new Error('No final answer');
        }

        this.updateState({ finalAnswer: this.state.finalAnswer });
        ConsoleLogger.success(`\nAGENT[${this.id}] ${this.state.finalAnswer}`);

        this.updateState({ messageHistory: formatMessageHistory(this.messageBuffer) });

        // Clean ups
        //this.updateState({ finalAnswer: null, completed: false , scratchpad: ''});

    }

    private async _step(): Promise<any> {
        ConsoleLogger.debug(`Current State: ${JSON.stringify(this.state)}`);
        // Build the context
        const context = buildContext(this.state, Templates.reactTemplate);
        ConsoleLogger.debug(`Context: ${context}`);

        // Build the system prompt
        const systemPrompt = buildContext(this.state, Templates.personalityTemplate);

        // Generate the response
        const response = await this.llmEngine.generateText(context, this.state?.model, systemPrompt);
        ConsoleLogger.debug(`Response: ${response}`);

        // Parse the response
        const parsedResponse = parseJSONBlock(response);
        ConsoleLogger.debug(`Parsed Response: ${JSON.stringify(parsedResponse)}`);

        if (!parsedResponse) {
            return null
        }

        // Update the scratchpad
        this.state.scratchpad = `${this.state.scratchpad}\nThought: ${parsedResponse.thought}`;

        // Limit scratchpad steps
        const steps = this.state.scratchpad.split('\n').filter((line: string) => line.trim());
        if (steps.length > this.STEPS_BUFFER_SIZE) {
            // Keep only the last 33 steps
            this.state.scratchpad = steps.slice(-this.STEPS_BUFFER_SIZE).join('\n');
        }

        // Execute the action
        if (parsedResponse.action && parsedResponse.action !== 'null') {
            this.state.scratchpad = `${this.state.scratchpad}\nAction: ${parsedResponse.action}[${parsedResponse.actionInput}]`;
            const tool = this.tools.find(tool => tool.name === parsedResponse.action);
            if (!tool) {
                ConsoleLogger.error(`Tool ${parsedResponse.action} not found`);
                this.state.scratchpad = `${this.state.scratchpad}\nObservation: Tool ${parsedResponse.action} not found`;
            }
            else {
                ConsoleLogger.debug(`Executing tool: ${tool.name}[${parsedResponse.actionInput}]`);
                const result = await tool.execute(parsedResponse.actionInput);
                ConsoleLogger.debug(`Tool result: ${result}`);
                this.state.scratchpad = `${this.state.scratchpad}\nObservation: ${result}`;
            }
        }

        if (parsedResponse.finalAnswer) {
            if (this.state.thought) {
                this.state.scratchpad = `${this.state.scratchpad}\nThought: ${this.state.thought}`;
            }
            this.state.scratchpad = `${this.state.scratchpad}\nFinal Answer: ${parsedResponse.finalAnswer}`;
            this.state.completed = true;
            this.updateState({ finalAnswer: parsedResponse.finalAnswer });
            return parsedResponse.finalAnswer;
        }

        return parsedResponse;
    }

    public addClient(client: IClient): void {
        this.clients.set(client.id, client);
    }

    public removeClient(id: string): void {
        this.clients.delete(id);
    }

    public getClients(): Map<string, IClient> {
        return this.clients;
    }

    public addTools(tools: ITool[]): void {
        this.tools = [...this.tools, ...tools];
    }

    public getTools(): ITool[] {
        return this.tools;
    }   

    public addProviders(providers: IProvider[]): void {
        this.providers = [...this.providers, ...providers];
    }

    public getProviders(): IProvider[] {
        return this.providers;
    } 

    public getState(): State {
        return this.state;
    }

    public updateState(state: State): void {
        this.state = { ...this.state, ...state };
    }

    public addMessage(message: Message): void {
        this.messageBuffer.push(message);
        if (this.messageBuffer.length > this.MESSAGE_BUFFER_SIZE) {
            this.messageBuffer.shift(); // Remove oldest message
        }
    }

    public getMessageHistory(): Message[] {
        return this.messageBuffer;
    }

    public async disconnectAllClients(): Promise<void> {
        for (const client of this.clients.values()) {
            await client.disconnect();
        }
    }
}
