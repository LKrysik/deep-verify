const { Command } = require('commander');
const path = require('node:path');

// Load package.json for version
const packageJson = require('../../package.json');

const program = new Command();

// Detect if called as 'dv' or 'qv' alias
const execName = path.basename(process.argv[1], '.js');

program
  .name('deep-verify')
  .description('Deep Verify - Systematic artifact verification using AI-powered analysis')
  .version(packageJson.version);

// Install command
program
  .command('install [target]')
  .description('Install Deep Verify module in a project')
  .action(async (target) => {
    const { installInteractive } = require('../installer/index.js');
    const success = await installInteractive(target || process.cwd());
    if (!success) {
      process.exit(1);
    }
  });

// Verify command (Deep Verify - full 6 phases)
program
  .command('verify <artifact>')
  .alias('dv')
  .description('Run full Deep Verify (6-phase verification)')
  .option('-s, --stakes <level>', 'Stakes level: low, medium, high')
  .option('-m, --mode <mode>', 'Verification mode: standard, blind')
  .option('-o, --output <path>', 'Output directory for report')
  .action(async (artifact, options) => {
    const verifyCommand = require('./commands/verify.js');
    await verifyCommand(artifact, options);
  });

// Quick command (Quick Verify - Phase 1 only)
program
  .command('quick <artifact>')
  .alias('qv')
  .description('Run Quick Verify (Phase 1 only with early exit)')
  .option('-m, --mode <mode>', 'Verification mode: standard, blind')
  .option('--no-early-exit', 'Disable early exit conditions')
  .action(async (artifact, options) => {
    const quickCommand = require('./commands/quick.js');
    await quickCommand(artifact, options);
  });

// Report command
program
  .command('report [subcommand] [argument]')
  .description('Manage verification reports (list, show, delete)')
  .action(async (subcommand, argument) => {
    const reportCommand = require('./commands/report.js');
    await reportCommand(subcommand, argument);
  });

// Config command
program
  .command('config [subcommand] [key] [value]')
  .description('Manage configuration (list, get, set)')
  .action(async (subcommand, key, value) => {
    const configCommand = require('./commands/config.js');
    await configCommand(subcommand, key, value);
  });

// Methods command
program
  .command('methods [id]')
  .description('List verification methods or show method details')
  .action(async (id) => {
    const methodsCommand = require('./commands/methods.js');
    await methodsCommand(id);
  });

// Patterns command
program
  .command('patterns [id]')
  .description('List impossibility patterns or show pattern details')
  .action(async (id) => {
    const patternsCommand = require('./commands/patterns.js');
    await patternsCommand(id);
  });

// Handle 'dv' and 'qv' aliases when called directly
if (execName === 'dv') {
  // Called as 'dv', treat remaining args as verify command
  const args = process.argv.slice(2);
  process.argv = [process.argv[0], process.argv[1], 'verify', ...args];
} else if (execName === 'qv') {
  // Called as 'qv', treat remaining args as quick command
  const args = process.argv.slice(2);
  process.argv = [process.argv[0], process.argv[1], 'quick', ...args];
}

// Parse and execute
program.parseAsync(process.argv).catch((error) => {
  console.error('Error:', error.message);
  process.exit(1);
});
