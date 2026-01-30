const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');
const { findProjectRoot, loadConfig } = require('../utils/config.js');
const logger = require('../utils/logger.js');

/**
 * Quick Verify command - Phase 1 only with early exit capability
 */
async function quickCommand(artifact, options) {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);

  logger.info('Quick Verify (QV) - Phase 1 Only');
  logger.log('');

  // Validate artifact path
  const artifactPath = path.isAbsolute(artifact) ? artifact : path.join(process.cwd(), artifact);

  if (!(await fs.pathExists(artifactPath))) {
    logger.error(`Artifact not found: ${artifactPath}`);
    process.exit(1);
  }

  logger.log(chalk.cyan('Artifact: ') + artifactPath);
  logger.log(chalk.cyan('Mode: ') + (options.mode || config.default_mode || 'standard'));
  logger.log('');

  // Output quick verification info
  logger.log(chalk.yellow('Quick Verification executes:'));
  logger.log('  - Phase 0: Setup (simplified)');
  logger.log('  - Phase 1: Pattern Scan with Tier 1 methods:');
  logger.log('      #71 First Principles Analysis');
  logger.log('      #100 Vocabulary Consistency');
  logger.log('      #17 Abstraction Laddering');
  logger.log('');

  logger.log(chalk.yellow('Early Exit Conditions:'));
  logger.log('  - S >= 6 + pattern match → REJECT');
  logger.log('  - S <= -3 + LOW/MEDIUM stakes → ACCEPT');
  logger.log('  - Otherwise → Recommend full DV');
  logger.log('');

  logger.warn('Note: Quick verification requires AI agent integration.');
  logger.log('');
  logger.log('To run quick verification with an AI agent:');
  logger.log(chalk.green('  1. Open your AI IDE (Claude Code, Cursor, Windsurf)'));
  logger.log(chalk.green('  2. Use command: /bmad:bmm:agents:deep-verifier'));
  logger.log(chalk.green('  3. Request "Quick Verify" mode'));
  logger.log(chalk.green(`  4. Provide artifact path: ${artifactPath}`));
}

module.exports = quickCommand;
