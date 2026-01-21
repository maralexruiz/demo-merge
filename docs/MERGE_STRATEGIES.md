# Git Merge Strategies Guide

This document explains different Git merge strategies and how to test them with this project.

## Overview

This project is designed to help you practice and understand different Git merge strategies. The simple calculator application provides a realistic codebase where you can create branches, make changes, and experiment with various merge approaches.

## Merge Strategies

### 1. Fast-Forward Merge

**When to use:** When your feature branch hasn't diverged from the main branch.

```bash
git checkout main
git merge feature-branch
```

**Test scenario:**
- Create a new branch from main
- Add a new operation to calculator.py
- Merge back to main (will be fast-forward if main hasn't changed)

### 2. Three-Way Merge (Recursive)

**When to use:** When both branches have diverged with different commits.

```bash
git checkout main
git merge feature-branch
```

**Test scenario:**
- Create branch `feature-A` and modify `utils.py`
- Switch to main and modify `calculator.py`
- Merge `feature-A` into main (creates a merge commit)

### 3. Squash Merge

**When to use:** When you want to combine all feature branch commits into a single commit.

```bash
git checkout main
git merge --squash feature-branch
git commit -m "Add feature X"
```

**Test scenario:**
- Create a branch with multiple commits
- Use squash merge to combine them into one commit on main

### 4. Rebase

**When to use:** When you want to maintain a linear history.

```bash
git checkout feature-branch
git rebase main
git checkout main
git merge feature-branch
```

**Test scenario:**
- Create a feature branch
- Make commits on both main and feature branch
- Rebase feature branch onto main
- Fast-forward merge to main

### 5. Cherry-Pick

**When to use:** When you want to apply specific commits from one branch to another.

```bash
git checkout main
git cherry-pick <commit-hash>
```

**Test scenario:**
- Create multiple commits on a feature branch
- Cherry-pick only specific commits to main

## Testing Merge Conflicts

### Creating Conflicts

Modify the same lines in different branches:

1. **Branch A:** Change version in calculator.py to "1.1.0"
2. **Branch B:** Change version in calculator.py to "1.2.0"
3. Attempt to merge - conflict!

### Resolving Conflicts

```bash
# After conflict occurs
git status  # See conflicting files
# Edit files to resolve conflicts
git add <resolved-files>
git commit
```

## Practice Scenarios

### Scenario 1: Feature Development
- Create `feature/add-power` branch
- Add a power operation to Calculator class
- Add tests for the new operation
- Merge using regular merge strategy

### Scenario 2: Hotfix
- Create `hotfix/divide-precision` branch from main
- Fix precision issue in divide operation
- Merge quickly using fast-forward or cherry-pick

### Scenario 3: Release Management
- Create `release/v1.1` branch
- Make version updates and documentation changes
- Create merge conflict scenario
- Practice conflict resolution

## Best Practices

1. **Always pull before creating a branch**
   ```bash
   git pull origin main
   git checkout -b new-feature
   ```

2. **Keep commits small and focused**
   - Each commit should have a single purpose
   - Write descriptive commit messages

3. **Test before merging**
   ```bash
   python -m pytest tests/
   ```

4. **Choose the right strategy**
   - Fast-forward: Simple, linear changes
   - Merge commit: Preserve branch history
   - Squash: Clean up feature branch history
   - Rebase: Linear history, but rewrites commits

5. **Document merge decisions**
   - Use meaningful merge commit messages
   - Explain why you chose a particular strategy

## Common Commands

```bash
# Check current branch and status
git status
git log --oneline --graph --all

# Create and switch to new branch
git checkout -b feature-name

# Merge strategies
git merge feature-name                    # Default merge
git merge --no-ff feature-name           # Force merge commit
git merge --squash feature-name          # Squash all commits
git merge --ff-only feature-name         # Only if fast-forward possible

# Abort a merge
git merge --abort

# View merge conflicts
git diff --name-only --diff-filter=U

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

## Project-Specific Test Cases

Use this calculator project to practice:

1. **Parallel Feature Development:** 
   - Branch A: Add modulo operation
   - Branch B: Add power operation
   - Merge both to main

2. **Bug Fix During Feature Development:**
   - Start feature branch
   - Bug found in main
   - Fix on main
   - Rebase or merge fix into feature branch

3. **Multiple Developers:**
   - Simulate multiple developers editing different files
   - Practice coordinating merges

4. **Configuration Changes:**
   - Modify config/app_config.json on different branches
   - Practice resolving JSON merge conflicts

## Resources

- [Git Documentation - Merge Strategies](https://git-scm.com/docs/merge-strategies)
- [Atlassian Git Merge Tutorial](https://www.atlassian.com/git/tutorials/using-branches/git-merge)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
