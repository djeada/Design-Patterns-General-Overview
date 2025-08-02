# Design Patterns & SOLID Principles - Complete Guide

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive collection of **Design Patterns** and **SOLID Principles** with detailed explanations, practical examples, and working Python implementations. This repository serves as both a learning resource and a reference guide for software engineers, students, and anyone interested in writing maintainable, flexible, and robust code.

## 📚 Table of Contents

- [🏗️ Repository Structure](#️-repository-structure)
- [🎯 Getting Started](#-getting-started)
- [🔧 Creational Patterns](#-creational-patterns)
- [🏛️ Structural Patterns](#️-structural-patterns)
- [🎭 Behavioral Patterns](#-behavioral-patterns)
- [🧱 SOLID Principles](#-solid-principles)
- [📖 General Resources](#-general-resources)
- [🚀 Running the Code](#-running-the-code)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🏗️ Repository Structure

```
Design-Patterns-General-Overview/
├── notes/              # 📖 Comprehensive documentation
│   ├── behavioural/    # Behavioral patterns explained
│   ├── creational/     # Creational patterns explained
│   ├── structural/     # Structural patterns explained
│   ├── solid/          # SOLID principles explained
│   └── general/        # General concepts and overviews
├── src/                # 💻 Working Python implementations
│   ├── behavioural/    # Behavioral pattern implementations
│   ├── creational/     # Creational pattern implementations
│   ├── structural/     # Structural pattern implementations
│   └── solid/          # SOLID principle demonstrations
└── README.md           # This file
```

## 🎯 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/djeada/Design-Patterns-General-Overview.git
   cd Design-Patterns-General-Overview
   ```

2. **Explore the documentation:**
   - Browse the `notes/` directory for detailed explanations
   - Each pattern includes intent, structure, use cases, and examples

3. **Run the implementations:**
   - Navigate to `src/` directory
   - Run any Python file to see the pattern in action

## 🔧 Creational Patterns

Creational patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

| Pattern | Purpose | Implementation | Documentation |
|---------|---------|----------------|---------------|
| **Abstract Factory** | Create families of related objects | [`abstract_factory.py`](src/creational/abstract_factory.py) | [`📖 Notes`](notes/creational/abstract_factory.md) |
| **Builder** | Construct complex objects step by step | [`builder.py`](src/creational/builder.py) | [`📖 Notes`](notes/creational/builder.md) |
| **Factory Method** | Create objects without specifying exact classes | [`factory_method.py`](src/creational/factory_method.py) | [`📖 Notes`](notes/creational/factory_method.md) |
| **Prototype** | Clone objects instead of creating new ones | [`prototype.py`](src/creational/prototype.py) | [`📖 Notes`](notes/creational/prototype.md) |
| **Singleton** | Ensure only one instance exists | [`singelton.py`](src/creational/singelton.py) | [`📖 Notes`](notes/creational/singelton.md) |

**Quick Start:**
```bash
# Run a specific pattern
python src/creational/builder.py

# Run all creational patterns demo
cd src/creational && python -c "
for pattern in ['abstract_factory', 'builder', 'factory_method', 'prototype', 'singelton']:
    print(f'\\n=== {pattern.upper()} ===')
    exec(open(f'{pattern}.py').read())
"
```

## 🏛️ Structural Patterns

Structural patterns deal with object composition, creating relationships between objects to form larger structures.

| Pattern | Purpose | Implementation | Documentation |
|---------|---------|----------------|---------------|
| **Adapter** | Allow incompatible interfaces to work together | [`adapter.py`](src/structural/adapter.py) | [`📖 Notes`](notes/structural/adapter_facade_vs_proxy_vs_bridge.md) |
| **Bridge** | Separate abstraction from implementation | [`bridge.py`](src/structural/bridge.py) | [`📖 Notes`](notes/structural/bridge.md) |
| **Composite** | Compose objects into tree structures | [`composite.py`](src/structural/composite.py) | [`📖 Notes`](notes/structural/composite.md) |
| **Decorator** | Add behavior to objects dynamically | [`decorator.py`](src/structural/decorator.py) | [`📖 Notes`](notes/structural/decorator.md) |
| **Facade** | Provide simplified interface to complex subsystem | [`facade.py`](src/structural/facade.py) | [`📖 Notes`](notes/structural/facade.md) |
| **Flyweight** | Share objects efficiently to save memory | [`flyweight.py`](src/structural/flyweight.py) | [`📖 Notes`](notes/structural/flyweight.md) |
| **Proxy** | Provide placeholder/surrogate for another object | [`proxy.py`](src/structural/proxy.py) | [`📖 Notes`](notes/structural/proxy.md) |

**Quick Start:**
```bash
# Run a specific pattern
python src/structural/composite.py

# Run all structural patterns demo
cd src/structural && python -c "
for pattern in ['adapter', 'bridge', 'composite', 'decorator', 'facade', 'flyweight', 'proxy']:
    print(f'\\n=== {pattern.upper()} ===')
    exec(open(f'{pattern}.py').read())
"
```

## 🎭 Behavioral Patterns

Behavioral patterns focus on communication between objects and the assignment of responsibilities.

| Pattern | Purpose | Implementation | Documentation |
|---------|---------|----------------|---------------|
| **Chain of Responsibility** | Pass requests along a chain of handlers | [`chain_of_responsibility.py`](src/behavioural/chain_of_responsibility.py) | [`📖 Notes`](notes/behavioural/chain_of_responsibility.md) |
| **Command** | Encapsulate requests as objects | [`command.py`](src/behavioural/command.py) | [`📖 Notes`](notes/behavioural/command.md) |
| **Interpreter** | Define grammar and interpret language | [`interpreter.py`](src/behavioural/interpreter.py) | [`📖 Notes`](notes/behavioural/interpreter.md) |
| **Iterator** | Access elements sequentially | [`iterator.py`](src/behavioural/iterator.py) | [`📖 Notes`](notes/behavioural/iterator.md) |
| **Mediator** | Define object interaction through mediator | [`mediator.py`](src/behavioural/mediator.py) | [`📖 Notes`](notes/behavioural/mediator.md) |
| **Memento** | Capture and restore object state | [`memento.py`](src/behavioural/memento.py) | [`📖 Notes`](notes/behavioural/memento.md) |
| **Observer** | Notify dependents of state changes | [`observer.py`](src/behavioural/observer.py) | [`📖 Notes`](notes/behavioural/observer.md) |
| **State** | Change behavior when internal state changes | [`state.py`](src/behavioural/state.py) | [`📖 Notes`](notes/behavioural/state.md) |
| **Strategy** | Encapsulate algorithms and make them interchangeable | [`strategy.py`](src/behavioural/strategy.py) | [`📖 Notes`](notes/behavioural/strategy.md) |
| **Template Method** | Define algorithm skeleton in base class | [`template_method.py`](src/behavioural/template_method.py) | [`📖 Notes`](notes/behavioural/template_method.md) |
| **Visitor** | Separate algorithms from object structure | [`visitor.py`](src/behavioural/visitor.py) | [`📖 Notes`](notes/behavioural/visitor.md) |

**Quick Start:**
```bash
# Run a specific pattern
python src/behavioural/observer.py

# Run all behavioral patterns demo  
cd src/behavioural && python -c "
patterns = ['chain_of_responsibility', 'command', 'interpreter', 'iterator', 'mediator', 'memento', 'observer', 'state', 'strategy', 'template_method', 'visitor']
for pattern in patterns:
    print(f'\\n=== {pattern.upper()} ===')
    exec(open(f'{pattern}.py').read())
"
```

## 🧱 SOLID Principles

SOLID principles are fundamental guidelines for writing maintainable, flexible, and robust object-oriented code.

| Principle | Acronym | Description | Implementation | Documentation |
|-----------|---------|-------------|----------------|---------------|
| **Single Responsibility** | **S** | A class should have only one reason to change | [`single_responsibility_principle.py`](src/solid/single_responsibility_principle.py) | [`📖 Notes`](notes/solid/single_responsibility_principle.md) |
| **Open/Closed** | **O** | Open for extension, closed for modification | [`open_closed_principle.py`](src/solid/open_closed_principle.py) | [`📖 Notes`](notes/solid/open_closed_principle.md) |
| **Liskov Substitution** | **L** | Subclasses should be substitutable for base classes | [`liskov_substitution_principle.py`](src/solid/liskov_substitution_principle.py) | [`📖 Notes`](notes/solid/liskov_substitution_principle.md) |
| **Interface Segregation** | **I** | Many specific interfaces > one general interface | [`interface_segregation_principle.py`](src/solid/interface_segregation_principle.py) | [`📖 Notes`](notes/solid/interface_segregation_principle.md) |
| **Dependency Inversion** | **D** | Depend on abstractions, not concretions | [`dependency_inversion_principle.py`](src/solid/dependency_inversion_principle.py) | [`📖 Notes`](notes/solid/dependency_inversion_principle.md) |

**Quick Start:**
```bash
# Run all SOLID principles demonstration
python src/solid/solid_demo.py

# Run individual principle
python src/solid/single_responsibility_principle.py
```

## 📖 General Resources

Additional resources to deepen your understanding:

- **[General Overview](notes/general/general_overview.md)** - Introduction to design patterns
- **[SOLID Overview](notes/solid/solid_overview.md)** - Complete guide to SOLID principles  
- **[Refactoring Examples](notes/general/refactoring_examples.md)** - Common refactoring techniques
- **[SOLID Principles Summary](notes/general/solid.md)** - Quick reference guide

## 🚀 Running the Code

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses only Python standard library)

### Run Individual Patterns
```bash
# Navigate to the project directory
cd Design-Patterns-General-Overview

# Run any specific pattern
python src/creational/builder.py
python src/structural/decorator.py
python src/behavioural/observer.py
python src/solid/dependency_inversion_principle.py
```

### Run All Patterns
```bash
# Run all creational patterns
find src/creational -name "*.py" -exec python {} \;

# Run all structural patterns  
find src/structural -name "*.py" -exec python {} \;

# Run all behavioral patterns
find src/behavioural -name "*.py" -exec python {} \;

# Run complete SOLID demonstration
python src/solid/solid_demo.py
```

### Interactive Learning
Each implementation includes:
- ✅ **Clear examples** with real-world scenarios
- ✅ **Detailed comments** explaining each step
- ✅ **Bad vs Good** implementations showing common mistakes
- ✅ **Console output** demonstrating the pattern in action

## 🎯 Key Features

- **📖 Comprehensive Documentation**: Every pattern includes detailed explanations with intent, structure, use cases, and implementation considerations
- **💻 Working Code Examples**: All patterns have complete, runnable Python implementations
- **🔄 Before/After Examples**: Shows both violations and correct implementations
- **🧪 Practical Scenarios**: Real-world examples and use cases
- **🎨 Clean Code**: Follows Python best practices and PEP 8 guidelines
- **📚 Educational Content**: Perfect for learning and teaching design patterns

## 🏆 Benefits

### For Learning:
- **Step-by-step progression** from basic to advanced patterns
- **Visual examples** with clear explanations
- **Common pitfalls** and how to avoid them
- **Best practices** and implementation guidelines

### For Development:
- **Improved code quality** through proven patterns
- **Better maintainability** with SOLID principles
- **Enhanced flexibility** in software design
- **Reduced complexity** through proper abstraction

## 🤝 Contributing

We welcome contributions! Here's how you can help improve this repository:

### Types of Contributions
- 🐛 **Bug fixes** in existing implementations
- 📖 **Documentation improvements** and clarifications  
- 💻 **New pattern implementations** or variants
- 🧪 **Additional examples** and use cases
- 🎨 **Code quality improvements** and optimizations
- 🌍 **Language translations** of documentation

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes following our guidelines
4. **Test** your implementations thoroughly
5. **Commit** your changes (`git commit -m 'Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### Contribution Guidelines
- Follow **Python PEP 8** style guidelines
- Include **comprehensive documentation** for new patterns
- Provide **working examples** with clear output
- Add **both notes and implementation** for new patterns
- Ensure **consistency** with existing code structure
- Include **docstrings** and **type hints** where appropriate

### Code Standards
```python
"""
Pattern Name Implementation
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class ExampleClass:
    """Clear docstring explaining the class purpose."""
    
    def __init__(self, param: str):
        self.param = param
    
    def method_name(self) -> str:
        """Clear docstring explaining what this method does."""
        return f"Result: {self.param}"
```

## 📚 Learning Resources & References

### Books
- **"Design Patterns: Elements of Reusable Object-Oriented Software"** - Gang of Four
- **"Clean Code: A Handbook of Agile Software Craftsmanship"** - Robert C. Martin
- **"Clean Architecture: A Craftsman's Guide to Software Structure"** - Robert C. Martin
- **"Refactoring: Improving the Design of Existing Code"** - Martin Fowler

### Online Resources
- [Martin Fowler's Website](https://martinfowler.com/) - Excellent articles on software design
- [Uncle Bob's Clean Coder Blog](http://cleancoder.com/) - SOLID principles and clean code practices
- [Python Patterns Guide](https://python-patterns.guide/) - Python-specific pattern implementations
- [JHU OOSE Lectures](https://pl.cs.jhu.edu/oose/lectures/design-patterns.shtml) - Academic perspective on design patterns

### Additional References
- [Software Architecture Patterns](https://en.wikipedia.org/wiki/List_of_software_architecture_styles_and_patterns) - Wikipedia comprehensive list
- [Patterns Presentations](https://github.com/skimedic/presentations/tree/main/Patterns/Current) - Conference presentations on patterns
- [Refactoring Guru](https://refactoring.guru/design-patterns) - Visual design pattern explanations
- [SourceMaking](https://sourcemaking.com/design_patterns) - Pattern examples and explanations

## 🌟 Acknowledgments

- **Gang of Four** for the foundational design patterns book
- **Robert C. Martin (Uncle Bob)** for SOLID principles and clean code practices
- **Martin Fowler** for refactoring principles and architectural patterns
- **Python Community** for excellent language design that makes patterns elegant
- **Contributors** who help improve this repository

## 📞 Support & Community

- **Issues**: [GitHub Issues](https://github.com/djeada/Design-Patterns-General-Overview/issues)
- **Discussions**: [GitHub Discussions](https://github.com/djeada/Design-Patterns-General-Overview/discussions)
- **Email**: For private inquiries
- **Stars**: If this repository helped you, please ⭐ star it!

## 📈 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/djeada/Design-Patterns-General-Overview)
![GitHub forks](https://img.shields.io/github/forks/djeada/Design-Patterns-General-Overview)
![GitHub issues](https://img.shields.io/github/issues/djeada/Design-Patterns-General-Overview)
![GitHub pull requests](https://img.shields.io/github/issues-pr/djeada/Design-Patterns-General-Overview)

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ **Commercial use** - Use this code in commercial projects
- ✅ **Modification** - Modify the code as needed
- ✅ **Distribution** - Share and distribute the code
- ✅ **Private use** - Use for personal projects
- ⚠️ **Attribution required** - Credit the original authors
- ❌ **No warranty** - Software is provided "as is"

---

<div align="center">

**🎯 Happy Coding! 🎯**

*"Design patterns are not about providing solutions, they're about providing a common vocabulary for discussing solutions."*

**Made with ❤️ for the developer community**

[⬆ Back to Top](#design-patterns--solid-principles---complete-guide)

</div>
