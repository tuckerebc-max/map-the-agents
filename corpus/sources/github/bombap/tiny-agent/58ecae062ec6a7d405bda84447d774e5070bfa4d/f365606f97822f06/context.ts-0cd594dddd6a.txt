import { IProvider, ITool, State, Message, IAgentPersonality } from "./types.ts";
import { ConsoleLogger } from "./console.ts";

export function buildContext(state: State, template: string): string {
    // Replace {{key}} with the value of the key in the state
    let context = template;
    for (const key in state) {
        // Skip if not a string
        if (typeof state[key] !== 'string') {
            continue;
        }
        const value = state[key];
        context = context.replace(`{{${key}}}`, value);
    }
    return context;
}

export function formatTools(tools: ITool[]): string {
    return tools.map(tool => `- ${tool.name}: ${tool.description}\n\t- Input Format: ${tool.inputFormat}\n\t- Input Examples: ${tool.inputExamples.join(', ')}`).join('\n');
}

export function formatToolsList(tools: ITool[]): string {
    return tools.map(tool => tool.name).join(', ');
}

export async function formatProviders(providers: IProvider[]): Promise<string> {
    // Run providers
    ConsoleLogger.debug(`Running ${providers.length} providers`);
    const results = await Promise.all(providers.map(provider => {
        ConsoleLogger.debug(`Running provider: ${provider.name}`);
        return provider.run();
    }));

    // Format the results
    return results.join('\n');
}

export function formatMessageHistory(messageHistory: Message[]): string {
    return messageHistory.map(message => `${message.role}: ${message.content}`).join('\n');
}

// Creates a personality prompt from an IAgentPersonality object
export function formatPersonality(personality: IAgentPersonality): string {
    const sections = [
        `# Identity\nName: ${personality.name}`,
        
        '# Biography',
        ...personality.bio.map(line => `- ${line}`),
        
        '# Background Lore',
        ...personality.lore.map(line => `- ${line}`),
        
        '# Personality Style',
        ...personality.style.map(line => `- ${line}`),
        
        '# Rules',
        ...personality.rules.map(line => `- ${line}`)
    ];

    return sections.join('\n\n');
}