# Contributing to Demo Merge

Thank you for your interest in contributing! This document is itself an exercise in practicing merge workflows.

## Ways to Contribute

Since this is a learning project, contributions can include:

1. **Adding new calculator operations** (power, square root, etc.)
2. **Adding new test cases**
3. **Improving documentation**
4. **Creating new merge practice scenarios**
5. **Adding features** (history, constants, etc.)
6. **Fixing bugs** (intentional ones for practice!)

## Contribution Workflow

This is the standard workflow you should practice:

### 1. Fork or Create a Branch

```bash
# For this repository, create a branch
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Keep changes focused and related
- Write tests for new functionality
- Update documentation as needed
- Follow the existing code style

### 3. Test Your Changes

```bash
# Run all tests
python tests/test_calculator.py
python tests/test_utils.py

# Or run all at once if pytest is installed
python -m pytest tests/ -v
```

### 4. Commit Your Changes

```bash
git add <changed-files>
git commit -m "Brief description of changes"
```

**Commit Message Guidelines:**
- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Reference issues if applicable

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Code Style

This project uses Python with standard PEP 8 style guidelines:

- Use 4 spaces for indentation
- Maximum line length: 79 characters for code
- Use docstrings for functions and classes
- Keep functions focused and simple

## Example Contributions

### Example 1: Adding a New Operation

**File:** `src/calculator.py`

```python
def power(self, base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent
```

**File:** `tests/test_calculator.py`

```python
def test_power(self):
    """Test power operation."""
    self.assertEqual(self.calc.power(2, 3), 8)
    self.assertEqual(self.calc.power(5, 0), 1)
    self.assertEqual(self.calc.power(2, -1), 0.5)
```

### Example 2: Improving Documentation

Update README.md, add examples, clarify instructions, or fix typos.

### Example 3: Adding a Configuration Option

**File:** `config/app_config.json`

```json
{
  "features": {
    "basic_operations": true,
    "advanced_operations": true,  // New feature
    "history": true                // New feature
  }
}
```

## Testing Guidelines

All contributions should include tests:

1. **New features** must have corresponding tests
2. **Bug fixes** should include a test that would have caught the bug
3. **All tests must pass** before submitting

Run tests with:
```bash
python tests/test_calculator.py
python tests/test_utils.py
```

## Documentation Guidelines

Update documentation when:

- Adding new features
- Changing existing behavior
- Adding new merge scenarios
- Improving clarity

Documentation files to consider:
- `README.md` - Overview and quick start
- `docs/MERGE_STRATEGIES.md` - Strategy explanations
- `docs/EXERCISES.md` - Practice exercises
- `docs/GETTING_STARTED.md` - Beginner guide

## Branch Naming Conventions

Use descriptive branch names:

- `feature/add-power-operation` - New features
- `bugfix/fix-division-precision` - Bug fixes
- `docs/improve-readme` - Documentation updates
- `test/add-edge-cases` - Test additions

## Merge Strategy for This Project

For practice purposes, you can experiment with different merge strategies:

- **Feature branches**: Use merge commits to preserve history
- **Bug fixes**: Can use fast-forward or cherry-pick
- **Documentation**: Squash merge for clean history

## Conflict Resolution

If you encounter merge conflicts:

1. Don't panic!
2. Review the conflicting sections carefully
3. Understand both changes
4. Choose the best solution (or combine both)
5. Test after resolving
6. Commit the resolution

## Questions or Problems?

This is a learning project, so:

- Experiments are encouraged
- Mistakes are learning opportunities
- Ask questions by creating issues
- Share your learning experiences

## Creating Practice Scenarios

Want to help others learn? Create realistic scenarios:

1. **Document a real-world problem** you've encountered
2. **Create a reproducible scenario** in this project
3. **Write step-by-step instructions** for solving it
4. **Add it to EXERCISES.md**

## Code of Conduct

This is a learning environment:

- Be respectful and patient
- Help others learn
- Share knowledge
- Celebrate mistakes as learning opportunities
- Ask questions

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Thank You!

Every contribution helps make this a better learning resource for everyone interested in mastering Git merge strategies!

---

**Remember:** The journey of mastering Git merges starts with a single commit! 🚀
