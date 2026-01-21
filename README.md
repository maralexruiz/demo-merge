# Demo Merge - Git Merge Strategy Testing Project

A simple Python calculator application designed to help you practice and understand different Git merge strategies and workflows.

## Purpose

This project was created to test and practice various Git merge strategies in a safe, controlled environment. It addresses common challenges encountered in real-world repositories during release management and collaborative development.

## Project Structure

```
demo-merge/
├── src/                    # Source code
│   ├── calculator.py      # Calculator class with basic operations
│   ├── utils.py           # Utility functions
│   └── main.py            # Main application entry point
├── tests/                 # Unit tests
│   ├── test_calculator.py # Calculator tests
│   └── test_utils.py      # Utility tests
├── config/                # Configuration files
│   └── app_config.json    # Application settings
├── docs/                  # Documentation
│   ├── MERGE_STRATEGIES.md # Guide to Git merge strategies
│   └── EXERCISES.md        # Hands-on practice exercises
└── README.md              # This file
```

## Features

- **Simple Calculator Application**: Basic arithmetic operations (add, subtract, multiply, divide)
- **Modular Design**: Separate files for different concerns (calculator logic, utilities, main)
- **Test Suite**: Unit tests to validate functionality before and after merges
- **Configuration**: JSON config file for practicing merge conflicts
- **Documentation**: Comprehensive guides and exercises

## Quick Start

### Running the Application

```bash
# Navigate to the src directory
cd src

# Run the calculator
python main.py
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python tests/test_calculator.py
```

## Learning Git Merge Strategies

This project is specifically designed to help you practice:

1. **Fast-Forward Merges** - Simple, linear merges
2. **Three-Way Merges** - Merging divergent branches
3. **Squash Merges** - Combining multiple commits
4. **Rebase Workflows** - Maintaining linear history
5. **Cherry-Picking** - Selecting specific commits
6. **Conflict Resolution** - Handling merge conflicts

### Get Started with Exercises

1. Read [docs/MERGE_STRATEGIES.md](docs/MERGE_STRATEGIES.md) for an overview of merge strategies
2. Follow the hands-on exercises in [docs/EXERCISES.md](docs/EXERCISES.md)
3. Experiment with creating branches and merging them in different ways

## Common Workflows to Practice

### Scenario 1: Feature Development
```bash
git checkout -b feature/new-operation
# Make changes
git checkout main
git merge feature/new-operation
```

### Scenario 2: Resolving Conflicts
```bash
# Create conflicting changes on two branches
git merge branch-with-conflict
# Resolve conflicts
git add .
git commit
```

### Scenario 3: Clean History with Rebase
```bash
git checkout feature-branch
git rebase main
git checkout main
git merge feature-branch
```

## Testing Your Merges

Always validate merges by running tests:

```bash
python -m pytest tests/ -v
```

All tests should pass before considering a merge successful.

## Tips for Using This Project

- Create backup branches before experimenting
- Use `git log --graph --oneline --all` to visualize history
- Practice on this project before applying techniques to real repositories
- Don't be afraid to make mistakes - that's how you learn!

## Background

This project was created in response to merge-related issues encountered during release management in production repositories. By practicing in this controlled environment, you can:

- Build confidence with Git merge operations
- Understand when to use different merge strategies
- Learn to resolve conflicts effectively
- Develop best practices for team collaboration

## Contributing

Feel free to:
- Add new calculator operations
- Create additional test scenarios
- Improve documentation
- Add more practice exercises

Each contribution can serve as a learning opportunity for practicing merges!

## License

This is a learning project - feel free to use it however you like!

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
