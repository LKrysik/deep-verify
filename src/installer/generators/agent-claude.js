/**
 * Claude CLI agent generator
 * Generates .claude/commands/deep-verify.md
 */
const fs = require('fs-extra');
const path = require('node:path');
const { getAgentContent } = require('./agent-base.js');

/**
 * Generate Claude CLI command file content
 * @param {Object} config - Installation config
 * @returns {string} Claude command file content (markdown with YAML frontmatter)
 */
function generateClaudeAgent(config) {
  const base = getAgentContent(config);

  return `---
name: '${base.name}'
description: '${base.description}'
---

# Deep Verifier Agent Activation

<agent-activation CRITICAL="TRUE">

## PRE-FLIGHT CHECKLIST

You are now **${base.alias}**, the ${base.title}.

**BEFORE ANYTHING ELSE:**

1. **READ CONFIG** from \`{project-root}/${base.configPath}\`
   - Note: pattern_domains, default_stakes

2. **LOAD WORKFLOW** from \`{project-root}/${base.workflowPath}\`
   - This is your execution guide

3. **DISPLAY MENU** and wait for user command:

   | Command | Description |
   |---------|-------------|
   | **DV** | ${base.commands[0].description} |
   | **QV** | ${base.commands[1].description} |

## PERSONA

**Role:** ${base.persona.role}

**Identity:** ${base.persona.identity}

**Communication Style:** ${base.persona.communicationStyle}

**Core Principles:**
${base.persona.principles.map((p) => `- ${p}`).join('\n')}

## CRITICAL RULES

1. **NO QUOTE = NO FINDING** - Every finding MUST cite exact text from the artifact
2. **Mandatory Phase 3** - Always perform adversarial review (except early exit with pattern match)
3. **OUTPUT = REPORT** - Your deliverable is a structured verification report
4. **DON'T NARRATE** - Execute, don't describe what you're about to do
5. **LOAD FILES WHEN NEEDED** - Read method procedures and data files as needed

</agent-activation>

## Usage

\`\`\`
/deep-verify [artifact-path-or-paste-content]
\`\`\`

After activation, type **DV** for full verification or **QV** for quick scan.
`;
}

/**
 * Write Claude agent file to target directory
 * @param {string} targetDir - Target project directory
 * @param {Object} config - Installation config
 * @param {Object} logger - Logger instance
 */
async function writeClaudeAgent(targetDir, config, logger) {
  const content = generateClaudeAgent(config);
  const targetPath = path.join(targetDir, '.claude', 'commands', 'deep-verify.md');

  await fs.ensureDir(path.dirname(targetPath));
  await fs.writeFile(targetPath, content);

  logger.log(`   ✓ Created .claude/commands/deep-verify.md`);
}

module.exports = {
  generateClaudeAgent,
  writeClaudeAgent,
};
