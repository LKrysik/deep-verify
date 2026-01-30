const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');
const { findProjectRoot, loadConfig } = require('../utils/config.js');
const logger = require('../utils/logger.js');

/**
 * Deep Verify command - full 6-phase verification
 */
async function verifyCommand(artifact, options) {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);

  logger.info('Deep Verify (DV) - Full 6-Phase Verification');
  logger.log('');

  // Validate artifact path
  const artifactPath = path.isAbsolute(artifact) ? artifact : path.join(process.cwd(), artifact);

  if (!(await fs.pathExists(artifactPath))) {
    logger.error(`Artifact not found: ${artifactPath}`);
    process.exit(1);
  }

  logger.log(chalk.cyan('Artifact: ') + artifactPath);
  logger.log(chalk.cyan('Mode: ') + (options.mode || config.default_mode || 'standard'));
  logger.log(chalk.cyan('Stakes: ') + (options.stakes || config.default_stakes || 'auto-detect'));
  logger.log('');

  // Output verification phases info
  logger.log(chalk.yellow('Verification Phases:'));
  logger.log('  Phase 0: Setup - Assess stakes, document biases');
  logger.log('  Phase 1: Pattern Scan - Execute Tier 1 methods');
  logger.log('  Phase 2: Targeted Analysis - Signal-based method selection');
  logger.log('  Phase 3: Adversarial Validation - Challenge own findings');
  logger.log('  Phase 4: Verdict - Calculate evidence score');
  logger.log('  Phase 5: Report - Generate structured report');
  logger.log('');

  logger.warn('Note: Full automated verification requires AI agent integration.');
  logger.log('');
  logger.log('To run verification with an AI agent:');
  logger.log(chalk.green('  1. Open your AI IDE (Claude Code, Cursor, Windsurf)'));
  logger.log(chalk.green('  2. Use command: /bmad:bmm:agents:deep-verifier'));
  logger.log(chalk.green(`  3. Provide artifact path: ${artifactPath}`));
  logger.log('');

  // Show workflow location
  const workflowPath = path.join(__dirname, '../../workflows/deep-verify/workflow.md');

  if (await fs.pathExists(workflowPath)) {
    logger.log(chalk.gray(`Workflow definition: ${workflowPath}`));
  }

  // Create output directory if needed
  const outputDir = path.join(projectRoot, config.reports_output_folder);
  if (!(await fs.pathExists(outputDir))) {
    await fs.ensureDir(outputDir);
    logger.log(chalk.gray(`Created reports directory: ${outputDir}`));
  }

  logger.log(chalk.gray(`Reports will be saved to: ${outputDir}`));
}

module.exports = verifyCommand;
