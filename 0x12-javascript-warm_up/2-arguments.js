#!/usr/bin/node
if (Process.argv.length === 0) {
    console.log('No argument');
} else if (Process.argv.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}