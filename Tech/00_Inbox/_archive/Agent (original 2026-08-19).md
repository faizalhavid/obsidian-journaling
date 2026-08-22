An AI Agent is software that can interact with its environment and perform actions to complete a defined goal. At its core, this works by having a large language model operating in a loop in real time. AI Agents can have access to tools, external services, or even other AI Agents to help reach their goals.

![[Pasted image 20260819192233.png]]
## The Agentic Loop
1. user enter a prompt into Claude Code.
2. Claude gathers the context it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
3. It takes action — for example, editing a file or running a command.
4. It verifies the results and determines whether they achieve what your prompt set out to do.
5. If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.
![[Pasted image 20260819192607.png]]

## Context Management
Managing context within Claude Code is crucial. Use `/compact` to summarize long sessions and `/clear` to start fresh. To use your context window effectively: be specific with your prompts, check what's consuming your current context, and use subagents to delegate tasks where you only need the result.

## Code Review
Use a subagent for an unbiased code review before pushing. Use `/commit-push-pr` to handle the full commit-to-PR flow in one step. And use `--from-pr` to resume work on a PR later. These are small features, but they remove a lot of friction from your daily workflow.

### The CLAUDE.md File
The difference between a frustrating Claude Code session and a productive one often comes down to context — and the CLAUDE.md file is how you provide that context. Start with your stack, your preferences, and your commands, then build from there as you go.
### An Example

```CLAUDE.md
# Project This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM. 
# Commands 
- Dev server: `pnpm dev` 
- Run tests: `pnpm test` 
- Lint: `pnpm lint` 
# Code Style 
- Use 2-space indentation 
- Prefer named exports 
- All API routes go in app/api/ 
- Use server actions instead of API routes where possible
```

## Subagent
Keeping your context window clean is one of the best ways to stay productive with Claude Code. With subagents, you can run an agent in the background to handle the heavy lifting and return just the answer to your main context window.
#### Further Customization
Subagents can be customized further. Here are some highlights:
- **Persistent memory** lets your subagent retain memory across conversations. This is great if you're using it consistently on the same projects.
- **Preload skills** into subagents by adding the `skill` key and listing skills by name. Note that unlike skills in your main conversation, the entire skill is loaded into context here.

## Skills 
## MCP
MCP connects Claude Code to your external tools and data sources. Add servers with `claude mcp add`. Scope them to your project with `.mcp.json` so your team gets them automatically. And keep an eye on context usage by disabling servers you're not actively using.
## Hooks
Hooks give you deterministic control over Claude Code's behavior. Use PostToolUse for auto-formatting and logging. Use PreToolUse to block dangerous operations. Configure them with `/hooks` or in `settings.json`. And check them into your repo so your team gets them too.
### How They Work
Hooks are configured in your `settings.json`. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. The available events are:

- **PreToolUse** — runs before a tool call
- **PostToolUse** — runs after a tool call completes
- **UserPromptSubmit** — runs when you submit a prompt, before Claude processes it
- **Stop** — runs when Claude finishes responding
- **Notification** — runs when Claude sends a notification

You configure them through the `/hooks` command inside Claude Code, or by editing `settings.json` directly.