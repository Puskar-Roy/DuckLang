# Contributing Guidelines

Thank you for your interest in contributing to this project! We welcome contributions of all kinds, including bug reports, feature requests, documentation improvements, and code enhancements. Please follow the guidelines below to ensure a smooth collaboration.

## How to Contribute

1. **Fork the Repository**

    Click the Fork button at the top-right of this repository.

    This creates a copy of the repository under your GitHub account.
   ![image](https://github.com/user-attachments/assets/f79fff7c-0c22-475c-80b6-581b4fabe66c)

2. **Clone Your Fork**

    Clone the forked repository to your local machine:

    ```sh
    git clone https://github.com/your-username/DuckLang.git
    ```

    Navigate into the project directory:

    ```sh
    cd DuckLang
    ```

3. **Create a New Branch**

    Create a branch for your changes:

    ```sh
    git checkout -b feature-branch-name
    ```

    Use a descriptive name related to the feature or bug you are addressing.

4. **Make Your Changes**

    Implement your feature, fix a bug, or improve documentation.

    Follow the project's coding style and best practices.

    Test your changes before committing.

5. **Commit Your Changes**

    Stage your changes:

    ```sh
    git add .
    ```

    Commit with a meaningful message:

    ```sh
    git commit -m "Add feature/fix bug: Brief description"
    ```

6. **Push to Your Fork**

    Push the changes to your forked repository:

    ```sh
    git push origin feature-branch-name
    ```

7. **Submit a Pull Request**

    Go to the original repository on GitHub.

    Click on Pull Requests > New Pull Request.

    Select your fork and branch, then compare with the base repository.

    Ensure you are making the pull request to the `dev` branch, not `master`.

    Add a meaningful title and description.

    Click Create Pull Request.

## Starting the Project

To start the project locally, follow these steps:

1. **Change Permission 🛃**

    ```sh
    chmod +x setup.sh
    ```

2. **Set Up The Project 🟰**

    ```sh
    ./setup.sh
    ```

3. **Start The Project 🚀**

    ```sh
    python main.py
    ```

## Directory Structure

Here is an overview of the project's directory structure:

```
DuckLang/
├── docs/
├── lib/
├── scripts/
├── src/
│   ├── interpreter/
    ├── lexer/
│   └── parser/
├── .gitignore
├── ducklangweb
├── main.py
├── requirements.txt
├── setup.sh
└── README.md
```

- `docs/`: Documentation files.
- `lib/`: Library files.
- `scripts/`: Utility scripts.
- `src/`: Contains the source code of the project.
- `interpreter/`: Interpreter module.
- `lexer/`: Lexer module.
- `parser/`: Parser module.
- `.gitignore`: Specifies files to be ignored by Git.
- `ducklangweb`: Web interface for DuckLang.
- `main.py`: Main application script.
- `requirements.txt`: Python dependencies.
- `setup.sh`: Setup script.
- `README.md`: Project documentation.

## Contribution Guidelines

- Follow proper coding style and format.
- Ensure your code is well-documented.
- Write meaningful commit messages.
- Add tests if applicable.
- Be respectful in discussions and reviews.

## Issues and Discussions

- Report bugs and suggest features via Issues.
- Discuss new ideas or improvements in the Discussions section.

## Need Help?

If you have any questions, feel free to open an issue or ask in the discussions.

Happy coding! 🚀
