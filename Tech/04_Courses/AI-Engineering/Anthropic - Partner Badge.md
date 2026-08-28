---
aliases: []
tags:
  - daily
status: draft
area: Meta
created: 2026-08-26
---

## What Claude Code is and how it behaves in a codebase

LESSON 1 OF 3 · PRODUCT FOUNDATIONS

# Claude Code: an agent _built for the codebase_

## 📑 Daftar Isi

- [Claude Code works inside the codebase](#claude-code-works-inside-the-codebase-that-changes-what-it-can-actually-do)
- [It reads, plans, acts, and checks with you](#it-reads-plans-acts-and-checks-with-you-before-it-keeps-going)
- [The CLI is the core](#the-cli-is-the-core-everything-else-is-a-wrapper-around-the-same-agent)

By the end of this lesson, you can explain what Claude Code is, how it operates inside a repository, and why that's different from a chat interface.

What it is

## Claude Code works inside the codebase. That changes what it can _actually do_.

Most AI tools sit outside the work. Claude Code sits inside it.

Chat interface

Answers questions. Generates text.

No access to your files, terminal, or project context. It's stateless between messages, useful for drafting and explaining but not for building.

Claude Code

Reads, edits, runs, and loops.

Reads and writes files directly, runs bash commands, and edits across the codebase. Maintains session context and keeps working until the task is done.

How it works

## It reads, plans, acts, and checks with you _before it keeps going_.

Claude Code doesn't generate code and stop. It works in a loop until the task is complete or you pause it.

1. Observe

Reads the relevant files, terminal context, and project history. Builds an understanding of the current state before planning anything.

In practice: it greps the codebase, opens the files it judges relevant, and reads recent terminal output. It does not assume the structure of your project; it looks first.

2. Plan

Breaks the task into steps. Decides which files to touch, which commands to run, and in what order.

For larger tasks it can surface the plan for your review before acting, so you approve the approach rather than reacting to changes after they land.

3. Act

Edits files, runs bash commands, calls tools. Every action is logged and visible in the terminal, not simulated output in a chat window.

Each tool call is a real operation on the machine. You see the diff, the command, and its output, which is what makes the work auditable rather than opaque.

4. Verify

Surfaces the result and waits for your approval. If something needs correcting, it loops back to Observe. You stay in control of the cycle.

Failed test? Unexpected output? It feeds that back into a fresh Observe pass and tries again, until the task is done or you pause it.

Verify feeds back into Observe. The loop runs until the task is **done** or you pause it.

The loop doesn't stop until the task is done or you pause it. Every tool call (file edit, bash command, search) is logged and reviewable. That's what makes autonomous operation safe to authorize.

Where it runs

## The CLI is the core. Everything else is a _wrapper around the same agent_.

Same model. Same agentic loop. The surface changes the integration point, not the intelligence.

The four surfaces share the same model and agent loop. One important distinction: the CLI has native filesystem and terminal access at the operating system level. Desktop, Web, and Mobile reach those same capabilities only when the developer explicitly invokes Claude Code's agent tooling from within those surfaces, not directly from the host OS. That difference in access surface matters when scoping what a deployment can do.

1. CLINative access

Native terminal access with the full Claude Code capability set. The primary interface for most developer workflows and the reference point for all configuration decisions.

**Access surface:** direct, at the operating-system level. Filesystem and terminal are available without any extra invocation. This is the baseline every other surface is measured against.

2. IDE ExtensionsNative access

Available for VS Code and JetBrains, surfacing the same agent inline with the editor. Reduces context switching without changing what Claude Code can do.

**Access surface:** same as the CLI, since the extension runs the local agent. The editor is a wrapper, not a lighter version of the product.

3. Agent SDKNative access

Programmatic access for pipeline and automation use cases. Lets engineering teams embed Claude Code into CI/CD, tooling, or multi-agent workflows.

**Access surface:** whatever the host environment grants. In CI/CD it has the runner's access; the scope is defined by where you run it.

4. Desktop / Web / MobileScoped access

Runs tasks in the cloud, without requiring a local environment. Suited for business-facing work that doesn't need filesystem or terminal access.

**Access surface:** reaches filesystem and terminal only when the developer explicitly invokes the agent tooling, not directly from the host OS. This is the distinction that matters when scoping a deployment.
