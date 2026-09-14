# [Demo Name]

[Summary]

## Components

This project is structured as a monorepository with a CDK backend and React frontend in the `src` folder. Modules that are unique to a certain CDK construct or React component are colocated (in the same parent folder). Shared or generic modules are found in a "common" folder.

### Backend

![architecture](architecture.drawio.png)

`bin/demo.ts` is the entrypoint to the CDK application. `lib/stacks` contains the application's stacks and child constructs.

#### [Frontend Stack](./src/backend/lib/stacks/frontend/index.ts)

- The static React website is hosted in a private Amazon S3 bucket and served using Amazon CloudFront with an Origin Access Control.
- Another S3 bucket is used for storing access logs.
- A CloudFront-scoped AWS Web Application Firewall (WAF) web access control list (ACL) protects the CloudFront distribution with the following managed rules: AWSManagedRulesCommonRuleSet, AWSManagedRulesAmazonIpReputationList, and AWSManagedRulesBotControlRuleSet.

#### [Backend Stack](./src/backend/lib/stacks/backend/index.ts)

##### [VPC](./src/backend/lib/stacks/backend/vpc.ts)

- An Amazon VPC with 3 subnets: one public, one private isolated, and one private with agress are created.
- Gateway and interface endpoints are used to provide secure connectivity to services like Amazon S3, DynamoDB, and Bedrock.
- A security group allows all outbound traffic and access from the client.

##### [Auth](./src/backend/lib/stacks/backend/auth.ts)

- An Amazon Cognito UserPool, UserPoolClient, and IdentityPool are used for authentication.
- A regional web ACL is created to protect Cognito and APIs.

##### [Graph API](./src/backend/lib/stacks/backend/graph-api/index.ts)

- The AWS Amplify GraphQL contruct is powered by AWS AppSync and connected to an Amazon DynamoDB database.
- A sample schema is provided to get you started.

##### [REST API](./src/backend/lib/stacks/backend/rest-api/index.ts)

- An Amazon API Gateway Lambda proxy integration, alongside Powertools for AWS Lambda, is used to enable the quick creation of new API routes without managing additional infrastructure.

##### [Storage](./src/backend/lib/stacks/backend/storage/index.ts)

- An Amazon S3 bucket is used to store other demo assets like images, videos, synthetic data, etc.

##### [Knowledge](./src/backend/lib/stacks/backend/knowledge.ts)

- Another Amazon S3 bucket is used as a Knowledge Base source, with a Knowledge Base construct simplifying GenAI infrastructure management.

#### [Frontend Deployment Stack](./src/backend/lib/stacks/frontend/index.ts)

- Website assets are uploaded to an Amazon S3 bucket from the `src/frontend` folder.
- A CDK custom resource provider triggers an Amazon CodeBuild project which builds the React application.

### Frontend

`src/index.tsx` is the entrypoint to the React application. `src/pages` contains the application's pages and child components.

- The frontend application uses [Vite React](https://vite.dev/guide/) and Amazon's [CloudScape design system](https://cloudscape.design/).
- The AWS CDK-created backend resources are linked to the frontend via [Amplify.configure](./src/frontend/src/App.tsx).
    - Amplify [Auth](https://docs.amplify.aws/vue/build-a-backend/auth/set-up-auth/) wraps the application, providing identity-based permissioning.
    - Amplify [API](https://docs.amplify.aws/gen1/javascript/build-a-backend/restapi/set-up-rest-api/) and [Storage](https://docs.amplify.aws/react/build-a-backend/storage/) are used to access a REST API and S3 bucket respectively.

## Pricing Estimation

| AWS Service                                                       | Pricing Considerations                  | Estimated Cost (USD) |
| ----------------------------------------------------------------- | --------------------------------------- | -------------------- |
| [Amazon S3](https://aws.amazon.com/s3/pricing/)                   | • Type of storage class                 | $                    |
|                                                                   | • Amount of storage per month           |                      |
|                                                                   | • Number of requests                    |                      |
|                                                                   | • Amount of data transfer out           |                      |
| [Amazon CloudFront](https://aws.amazon.com/cloudfront/pricing/)   | • Amount of data transfer out by region | $                    |
|                                                                   | • Number of requests                    |                      |
|                                                                   | • Type of price class                   |                      |
| [AWS WAF](https://aws.amazon.com/waf/pricing/)                    | • Number of Web ACLs created            | $                    |
|                                                                   | • Number of rules per ACL               |                      |
|                                                                   | • Number of requests                    |                      |
| [Amazon Cognito](https://aws.amazon.com/cognito/pricing/)         | • Number of monthly active users        | $                    |
|                                                                   | • Type of pricing tier                  |                      |
|                                                                   | • Type of identity provider             |                      |
|                                                                   | • Number of SMS/email messages          |                      |
| [Amazon API Gateway](https://aws.amazon.com/api-gateway/pricing/) | • Number of requests                    | $                    |
|                                                                   | • Amount of data transfer               |                      |
| [AWS AppSync](https://aws.amazon.com/appsync/pricing/)            | • Number of queries                     | $                    |
|                                                                   | • Number of real-time updates           |                      |
|                                                                   | • Number of connection minutes          |                      |
|                                                                   | • Type of cache instance                |                      |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/pricing/)       | • Type of capacity mode                 | $                    |
|                                                                   | • Number of read/write units            |                      |
|                                                                   | • Amount of storage                     |                      |
| [AWS Lambda](https://aws.amazon.com/lambda/pricing/)              | • Number of requests                    | $                    |
|                                                                   | • Duration of compute                   |                      |
|                                                                   | • Amount of memory allocated            |                      |
| [Amazon VPC](https://aws.amazon.com/vpc/pricing/)                 | • Number of NAT Gateway hours           | $                    |
|                                                                   | • Amount of data processing             |                      |
|                                                                   | • Amount of data transfer               |                      |
| [AWS CodeBuild](https://aws.amazon.com/codebuild/pricing/)        | • Number of build minutes               | $                    |
|                                                                   | • Type of compute                       |                      |

For more details, visit the [AWS Pricing Calculator](https://calculator.aws/#/).

## Getting Started

### Prerequisites

- Install [Node](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), [Python](https://www.python.org/downloads/), [Docker](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html#install-docker-instructions), and the [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) then complete the [prerequisites for CDK deployments](https://docs.aws.amazon.com/cdk/v2/guide/deploy.html#deploy-prerequisites) if you have not previously done so.

### Deployment

- Open a terminal and set the working directory to the location where you want to clone this repository. Clone the repository using the command `git clone [url]`.
- From the root directory, run the command `npm run setup` to install the [CDK](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-typescript.html#work-with-cdk-typescript-dependencies) and React dependencies.
- [Deploy the CDK application](https://docs.aws.amazon.com/cdk/v2/guide/deploy.html#deploy-how-deploy) using a command like `npm run -w backend cdk deploy --all`.

## Clean-up

- Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home) then select each stack you created and click **Delete** twice. Or use [`cdk destroy`](https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-destroy.html).

## License

[Apache License Version 2.0](/LICENSE)
