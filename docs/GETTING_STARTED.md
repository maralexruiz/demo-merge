# Getting Started with Demo Merge

Welcome! This guide will help you get started with the demo-merge project.

## What You'll Learn

This project will teach you how to:
- Create and manage Git branches
- Perform different types of merges
- Resolve merge conflicts
- Choose the right merge strategy for different scenarios

## Prerequisites

- Git installed on your computer
- Python 3.6 or higher (for running the application)
- Basic understanding of Git commands (commit, branch, checkout)

## Initial Setup

1. **Clone or pull the latest changes**
   ```bash
   git pull origin main
   ```

2. **Verify the structure**
   ```bash
   ls -la
   # You should see: src/, tests/, docs/, config/, README.md
   ```

3. **Run the tests to ensure everything works**
   ```bash
   python tests/test_calculator.py
   python tests/test_utils.py
   ```

4. **Try running the application**
   ```bash
   cd src
   python main.py
   # Type 'quit' to exit
   ```

## Your First Merge Exercise

Let's do a simple exercise to get you started:

### Step 1: Create a Feature Branch

```bash
git checkout main
git pull  # Make sure you're up to date
git checkout -b my-first-feature
```

### Step 2: Make a Simple Change

Edit `src/calculator.py` and add a new method:

```python
def square(self, a):
    """Calculate the square of a number."""
    return a * a
```

### Step 3: Commit Your Change

```bash
git add src/calculator.py
git commit -m "Add square operation to calculator"
```

### Step 4: Merge Back to Main

```bash
git checkout main
git merge my-first-feature
```

**Congratulations!** You just completed your first merge! 🎉

## Next Steps

1. **Read the documentation**
   - Start with [docs/MERGE_STRATEGIES.md](MERGE_STRATEGIES.md) to understand different merge strategies
   - Review [docs/EXERCISES.md](EXERCISES.md) for more practice scenarios

2. **Practice conflict resolution**
   - Try Exercise 3 in EXERCISES.md to practice resolving merge conflicts

3. **Experiment with different strategies**
   - Practice squash merges
   - Try rebasing
   - Learn when to use each approach

## Common Commands Quick Reference

```bash
# Create and switch to a new branch
git checkout -b branch-name

# Switch to an existing branch
git checkout branch-name

# View all branches
git branch -a

# View commit history
git log --oneline --graph --all

# Merge a branch into current branch
git merge branch-name

# Abort a merge if something goes wrong
git merge --abort

# View current status
git status

# View changes
git diff
```

## Tips for Learning

1. **Don't be afraid to experiment** - You can always reset or create a new clone
2. **Use git log frequently** - Visualize what's happening with `git log --graph --oneline --all`
3. **Practice, practice, practice** - The more merges you do, the more comfortable you'll become
4. **Make mistakes intentionally** - Create conflicts on purpose to learn how to resolve them
5. **Read the error messages** - Git usually tells you what went wrong and how to fix it

## Getting Help

- Check the documentation in the `docs/` folder
- Use `git --help` or `git <command> --help` for command-specific help
- Review the README.md for project overview
- Practice the exercises in order - they build on each other

## Troubleshooting

**Problem:** Tests fail
```bash
# Make sure you're in the project root
cd /path/to/demo-merge
python tests/test_calculator.py
```

**Problem:** Can't find modules when running main.py
```bash
# Make sure you're in the src directory
cd src
python main.py
```

**Problem:** Merge conflict seems impossible to resolve
```bash
# You can always abort and try again
git merge --abort
```

**Problem:** Made a mistake and want to start over
```bash
# Reset your branch to match main
git checkout main
git branch -D problematic-branch
git checkout -b new-clean-branch
```

## Safety Tips

- Always commit your changes before attempting a merge
- Create backup branches for important work: `git branch backup-name`
- Use `git status` frequently to understand what state you're in
- Test after merging: run the tests to ensure nothing broke

## What to Do After This Guide

1. Complete Exercise 1-3 in [EXERCISES.md](EXERCISES.md)
2. Read through [MERGE_STRATEGIES.md](MERGE_STRATEGIES.md)
3. Try creating your own scenarios
4. Practice with a team member (simulate collaborative development)

## Happy Merging!

Remember: The goal is to learn by doing. Don't worry about making mistakes - that's the whole point of this practice project!

---

**Need more help?** Review the documentation files or examine the code to understand how everything works together.
