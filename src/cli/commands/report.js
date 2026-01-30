const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');
const { findProjectRoot, loadConfig } = require('../utils/config.js');
const logger = require('../utils/logger.js');

/**
 * List verification reports
 */
async function listReports() {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);
  const reportsDir = path.join(projectRoot, config.reports_output_folder);

  if (!(await fs.pathExists(reportsDir))) {
    logger.warn('No reports directory found.');
    logger.log(`Expected at: ${reportsDir}`);
    return;
  }

  const files = await fs.readdir(reportsDir);
  const reports = files.filter((f) => f.endsWith('.md') || f.endsWith('.json'));

  if (reports.length === 0) {
    logger.info('No verification reports found.');
    return;
  }

  logger.info(`Verification Reports (${reports.length}):`);
  logger.log('');

  for (const report of reports) {
    const reportPath = path.join(reportsDir, report);
    const stats = await fs.stat(reportPath);
    const date = stats.mtime.toISOString().split('T')[0];
    logger.log(`  ${chalk.cyan(report)} ${chalk.gray(`(${date})`)}`);
  }

  logger.log('');
  logger.log(chalk.gray(`Reports directory: ${reportsDir}`));
}

/**
 * Show a specific report
 */
async function showReport(reportId) {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);
  const reportsDir = path.join(projectRoot, config.reports_output_folder);

  // Try to find the report file
  let reportPath = path.join(reportsDir, reportId);

  if (!(await fs.pathExists(reportPath))) {
    // Try with .md extension
    reportPath = path.join(reportsDir, `${reportId}.md`);
  }

  if (!(await fs.pathExists(reportPath))) {
    logger.error(`Report not found: ${reportId}`);
    logger.log('');
    logger.log('Use `deep-verify report list` to see available reports.');
    process.exit(1);
  }

  const content = await fs.readFile(reportPath, 'utf8');
  console.log(content);
}

/**
 * Delete a report
 */
async function deleteReport(reportId) {
  const projectRoot = findProjectRoot();
  const config = await loadConfig(projectRoot);
  const reportsDir = path.join(projectRoot, config.reports_output_folder);

  let reportPath = path.join(reportsDir, reportId);

  if (!(await fs.pathExists(reportPath))) {
    reportPath = path.join(reportsDir, `${reportId}.md`);
  }

  if (!(await fs.pathExists(reportPath))) {
    logger.error(`Report not found: ${reportId}`);
    process.exit(1);
  }

  await fs.remove(reportPath);
  logger.success(`Deleted: ${path.basename(reportPath)}`);
}

/**
 * Report command router
 */
async function reportCommand(subcommand, argument) {
  switch (subcommand) {
    case 'list': {
      await listReports();
      break;
    }
    case 'show': {
      if (!argument) {
        logger.error('Please specify a report ID');
        logger.log('Usage: deep-verify report show <report-id>');
        process.exit(1);
      }
      await showReport(argument);
      break;
    }
    case 'delete': {
      if (!argument) {
        logger.error('Please specify a report ID');
        logger.log('Usage: deep-verify report delete <report-id>');
        process.exit(1);
      }
      await deleteReport(argument);
      break;
    }
    default: {
      // Default to list
      await listReports();
    }
  }
}

module.exports = reportCommand;
