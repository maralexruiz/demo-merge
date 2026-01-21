# Practice Exercises

This document contains hands-on exercises to practice different Git merge scenarios.

## Exercise 1: Simple Fast-Forward Merge

**Objective:** Practice the simplest merge scenario.

**Steps:**
1. Ensure you're on main and it's up to date
   ```bash
   git checkout main
   git pull
   ```

2. Create a new feature branch
   ```bash
   git checkout -b feature/add-modulo
   ```

3. Add a modulo operation to `src/calculator.py`:
   ```python
   def modulo(self, a, b):
       """Calculate a modulo b."""
       if b == 0:
           raise ValueError("Cannot calculate modulo with zero")
       return a % b
   ```

4. Commit your changes
   ```bash
   git add src/calculator.py
   git commit -m "Add modulo operation to calculator"
   ```

5. Switch back to main and merge
   ```bash
   git checkout main
   git merge feature/add-modulo
   ```

**Expected result:** A fast-forward merge (assuming main hasn't changed).

## Exercise 2: Three-Way Merge

**Objective:** Practice merging when both branches have diverged.

**Steps:**
1. Create a feature branch and make changes
   ```bash
   git checkout -b feature/improve-banner
   ```
   
2. Edit `src/utils.py` to improve the banner

3. Commit your changes
   ```bash
   git commit -am "Improve application banner"
   ```

4. Switch to main and make different changes
   ```bash
   git checkout main
   ```
   
5. Edit `src/calculator.py` to add version logging

6. Commit your changes
   ```bash
   git commit -am "Add version logging to calculator"
   ```

7. Merge the feature branch
   ```bash
   git merge feature/improve-banner
   ```

**Expected result:** A three-way merge with a merge commit.

## Exercise 3: Resolving Merge Conflicts

**Objective:** Practice identifying and resolving merge conflicts.

**Steps:**
1. Create branch A
   ```bash
   git checkout -b feature/version-1.1
   ```

2. Edit `src/calculator.py` and change version to "1.1.0"
   ```bash
   git commit -am "Update version to 1.1.0"
   ```

3. Switch to main and create branch B
   ```bash
   git checkout main
   git checkout -b feature/version-1.2
   ```

4. Edit `src/calculator.py` and change version to "1.2.0"
   ```bash
   git commit -am "Update version to 1.2.0"
   ```

5. Try to merge branch A into branch B
   ```bash
   git merge feature/version-1.1
   ```

**Expected result:** A merge conflict!

6. Resolve the conflict by editing the file

7. Complete the merge
   ```bash
   git add src/calculator.py
   git commit
   ```

## Exercise 4: Squash Merge

**Objective:** Practice combining multiple commits into one.

**Steps:**
1. Create a feature branch
   ```bash
   git checkout main
   git checkout -b feature/add-power
   ```

2. Add power operation (commit 1)
   ```bash
   # Edit calculator.py
   git commit -am "Add power operation stub"
   ```

3. Add error handling (commit 2)
   ```bash
   # Edit calculator.py
   git commit -am "Add error handling for power operation"
   ```

4. Add tests (commit 3)
   ```bash
   # Edit tests/test_calculator.py
   git commit -am "Add tests for power operation"
   ```

5. Switch to main and squash merge
   ```bash
   git checkout main
   git merge --squash feature/add-power
   git commit -m "Add power operation with tests and error handling"
   ```

**Expected result:** All three commits combined into one on main.

## Exercise 5: Rebase Workflow

**Objective:** Practice maintaining a linear history with rebase.

**Steps:**
1. Create a feature branch
   ```bash
   git checkout -b feature/add-logging
   ```

2. Make some commits on the feature branch

3. Simulate other work on main
   ```bash
   git checkout main
   # Make some changes
   git commit -am "Update documentation"
   ```

4. Rebase feature branch onto main
   ```bash
   git checkout feature/add-logging
   git rebase main
   ```

5. If conflicts occur, resolve them:
   ```bash
   # Fix conflicts
   git add .
   git rebase --continue
   ```

6. Fast-forward merge to main
   ```bash
   git checkout main
   git merge feature/add-logging
   ```

**Expected result:** Linear commit history without merge commits.

## Exercise 6: Cherry-Pick

**Objective:** Practice selectively applying commits.

**Steps:**
1. Create a feature branch with multiple commits
   ```bash
   git checkout -b feature/multiple-changes
   # Make commit 1: Add feature A
   # Make commit 2: Add feature B  
   # Make commit 3: Add feature C
   ```

2. Find the commit hash of feature B
   ```bash
   git log --oneline
   ```

3. Switch to main and cherry-pick only feature B
   ```bash
   git checkout main
   git cherry-pick <commit-hash-of-feature-B>
   ```

**Expected result:** Only the changes from feature B are applied to main.

## Exercise 7: Merge Conflict in Configuration

**Objective:** Practice resolving conflicts in JSON files.

**Steps:**
1. Create two branches that modify `config/app_config.json` differently

2. Try to merge them and resolve the JSON conflict carefully

3. Ensure the resulting JSON is valid
   ```bash
   python -c "import json; json.load(open('config/app_config.json'))"
   ```

## Exercise 8: Testing Before Merge

**Objective:** Practice validating changes before merging.

**Steps:**
1. Create a feature branch with new functionality

2. Before merging, run tests
   ```bash
   python -m pytest tests/ -v
   ```

3. Only merge if tests pass

4. After merging, run tests again on main
   ```bash
   git checkout main
   git merge feature-branch
   python -m pytest tests/ -v
   ```

## Completion Checklist

- [ ] Exercise 1: Fast-Forward Merge
- [ ] Exercise 2: Three-Way Merge
- [ ] Exercise 3: Resolving Conflicts
- [ ] Exercise 4: Squash Merge
- [ ] Exercise 5: Rebase Workflow
- [ ] Exercise 6: Cherry-Pick
- [ ] Exercise 7: Config File Conflicts
- [ ] Exercise 8: Testing Before Merge

## Tips

- Always check `git status` before and after operations
- Use `git log --graph --oneline --all` to visualize branch history
- Practice on this demo project before applying to real projects
- Don't be afraid to experiment - you can always reset to a previous state
- Create backups of important branches before experimenting
