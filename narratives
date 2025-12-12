CS 499 Milestone Two: Software Design and Engineering Enhancement
Narrative

Student Name: Trevor Hegge
Date: December 10, 2025
Course: CS 499 - Computer Science Capstone


Artifact Description

The artifact I selected for the software design and engineering category is a Task Management Application originally created in CS 320 - Software Engineering. This command-line Python application allows users to manage daily tasks through basic CRUD (Create, Read, Update, Delete) operations. The original artifact was developed as a course project to demonstrate fundamental programming concepts, but it suffered from significant structural flaws including the use of global variables, absence of error handling, lack of data persistence, and poor code organization with repeated logic blocks.


Justification for Inclusion

I selected this artifact for my ePortfolio because it provided an excellent opportunity to demonstrate my growth in software engineering principles and my ability to transform a functional but flawed application into a professional-quality product. The enhancement process showcases several critical skills valued in the software development industry. First, the refactoring from procedural code with global variables to an object-oriented design with proper encapsulation demonstrates my understanding of design patterns and clean code principles. Second, the implementation of comprehensive error handling with try-except blocks and input validation illustrates my commitment to creating robust, production-ready software. Third, adding JSON-based data persistence transforms the application from a temporary utility into a practical tool that maintains state between sessions.

The specific components that showcase my software development abilities include the newly implemented Task and TaskManager classes that eliminate global state, the comprehensive input validation system that prevents crashes from invalid user input, the JSON serialization module that enables data persistence, and the refactored helper method findTaskById() that eliminates code duplication. These improvements directly address the weaknesses identified in my code review, transforming lines 7-8's global variables into encapsulated class attributes, replacing the crash-prone int(input()) calls at lines 97, 103, and 106 with validated input functions, and consolidating the repeated search logic from lines 25-27, 34-36, and 58-60 into a single reusable method.


Course Outcomes Achievement

This enhancement successfully meets the course outcomes I planned to address in Module One. Course Outcome 3 (Design and evaluate computing solutions using algorithmic principles and computer science practices) is demonstrated through my implementation of object-oriented design patterns that solve the structural problems inherent in the original procedural approach. The decision to separate concerns between the Task class (data representation) and TaskManager class (business logic) reflects industry-standard software architecture practices. Course Outcome 4 (Use well-founded and innovative techniques, skills, and tools in computing practices) is evidenced by my adoption of Python's json module for data persistence, implementation of context managers for file operations, and use of list comprehensions for efficient data filtering. Course Outcome 5 (Develop a security mindset that anticipates adversarial exploits) is addressed through comprehensive input validation that prevents injection attacks, validates data types before processing, and sanitizes user input to prevent unexpected behavior.


Reflection on the Enhancement Process

The process of enhancing this artifact taught me valuable lessons about the importance of defensive programming and thoughtful software architecture. The most significant learning occurred when I attempted to implement the JSON persistence layer—I initially struggled with serializing the Task objects because Python's json module cannot directly serialize custom class instances. This challenge forced me to implement custom serialization methods (to_dict() and from_dict()) that convert Task objects to dictionaries for storage and reconstruct them when loading. This experience taught me that data persistence requires careful consideration of data formats and the relationship between in-memory representations and storage formats. Another key learning was recognizing how proper error handling dramatically improves user experience; by wrapping input operations in try-except blocks and providing clear error messages, the application became significantly more user-friendly and professional.

The primary challenge I faced was maintaining backward compatibility with the original functionality while completely restructuring the codebase. I needed to ensure that all seven menu options from the original application still worked correctly after refactoring to OOP design, which required extensive testing of each function. Additionally, implementing comprehensive input validation required me to think through numerous edge cases: What happens if someone enters an empty task name? What if they enter a future date in an invalid format? What if they try to complete a task that doesn't exist? Addressing these scenarios systematically improved my ability to anticipate potential failures and write defensive code. Another challenge was deciding the appropriate level of abstraction for the class design—I initially considered implementing separate classes for different task types, but I determined this would be over-engineering for the current scope. This decision-making process reinforced the importance of balancing robust design with practical simplicity.

Overall, this enhancement transformed my understanding of software engineering from simply "making code work" to "making code maintainable, robust, and professional." The artifact now represents work I would be proud to deploy in a production environment and effectively demonstrates my capabilities in software design and engineering for potential employers reviewing my ePortfolio.
