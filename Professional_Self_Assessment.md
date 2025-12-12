# Professional Self-Assessment

**Trevor Hegge**  
**CS 499 - Computer Science Capstone**  
**Southern New Hampshire University**  
**December 2025**

---

## Introduction

Completing my coursework throughout the Computer Science program at Southern New Hampshire University and developing this ePortfolio has been a transformative experience that has prepared me to enter the computer science field with confidence and a well-rounded skill set. Through the process of selecting, reviewing, and enhancing three key artifacts, I have gained a deeper understanding of my strengths and identified areas where I have grown significantly as a developer. This ePortfolio showcases my ability to write secure, efficient, and well-structured code while demonstrating my capacity to communicate technical concepts effectively to diverse audiences.

## Showcasing Strengths and Shaping Professional Goals

Throughout this program, I have developed strengths in several critical areas of computer science. My work on the Task Management Application enhancement demonstrated my ability to transform poorly structured procedural code into well-designed object-oriented systems. This experience taught me that good software engineering is not just about making code work, but about making it maintainable, scalable, and understandable by other developers. I learned to value clean code principles and design patterns that I had previously only read about in textbooks but now understand through hands-on implementation.

The Student Records System enhancement revealed my capability to analyze computational complexity and implement dramatic performance improvements. When I calculated that replacing bubble sort with efficient algorithms could make the application 1,000 times faster for large datasets, I realized that algorithmic knowledge has real-world impact. This project helped me understand that computer science is fundamentally about solving problems efficiently, and that theoretical knowledge of Big O notation translates directly into better user experiences. I now approach every coding problem by first considering the algorithmic implications of my design choices.

Perhaps most significantly, the Inventory Management System enhancement taught me about the critical importance of security in software development. Discovering seven SQL injection vulnerabilities in my original code was humbling, but fixing them gave me confidence that I can identify and eliminate security flaws. I learned that security is not an afterthought but must be integrated into every stage of development. This experience shaped my professional goal to become a developer who prioritizes security from the beginning of every project, understanding that protecting user data is a fundamental responsibility.

My experiences with team projects in courses like CS 250 (Software Development Lifecycle) taught me the value of collaboration in software development. Working on agile teams, I learned to communicate my ideas clearly during stand-up meetings, provide constructive code review feedback to peers, and incorporate others' suggestions into my work. One particularly memorable experience was when a teammate pointed out a logic error in my code during a review session. Initially defensive, I realized that their perspective helped me catch a bug before it reached production. This taught me that collaboration makes everyone's code better and that diverse viewpoints strengthen software quality.

## Technical Skills and Competencies

### Collaborating in Team Environments

My ability to work effectively in collaborative environments has developed through both coursework and the ePortfolio creation process. In CS 320 (Software Testing and Quality Assurance), I participated in peer code reviews where I learned to provide specific, actionable feedback rather than vague criticism. For example, instead of saying "this function is confusing," I learned to say "this function would be clearer if it were split into two methods, each handling one responsibility." This experience directly informed my code review video for this capstone, where I systematically analyzed my artifacts and explained my enhancement plans in a way that peers or managers could understand.

Throughout the program, I have also learned the importance of clear documentation and in-code comments. My enhanced artifacts include comprehensive docstrings that explain not just what each function does, but why certain design decisions were made. For instance, in my Inventory Management System, I added comments explaining why I chose ON DELETE SET NULL instead of ON DELETE CASCADE for foreign key relationships—this kind of documentation helps future developers (including my future self) understand the reasoning behind technical choices.

### Communicating with Stakeholders

The ability to communicate effectively with both technical and non-technical stakeholders has been crucial throughout my program. In my code review video, I practiced explaining complex technical concepts—like SQL injection vulnerabilities and computational complexity—in terms that a manager without deep technical knowledge could understand. Rather than saying "the code has O(n²) complexity," I explained "this sorting method is 1,000 times slower than it needs to be for large datasets, which would frustrate users."

My narratives for each artifact enhancement demonstrate my ability to reflect on my learning process and explain technical improvements in clear, professional writing. I learned to structure my thoughts logically, support my claims with specific evidence, and connect my work to broader course outcomes. This skill will be invaluable when I need to write technical documentation, project proposals, or status reports in my professional career.

### Data Structures and Algorithms

My work on the Student Records System enhancement deepened my understanding of how data structure choices impact application performance. Before this project, I understood hash tables theoretically, but implementing the conversion from a list-based structure to a dictionary-based structure made the benefits concrete. When I measured that ID searches became 10,000 times faster with O(1) hash table lookups versus O(n) linear search, I truly grasped why data structures matter.

I also learned that choosing the right algorithm for a specific problem is more important than memorizing sorting algorithms. The findTopStudents function originally sorted the entire dataset just to find the top five students—an inefficient approach I had not recognized as problematic until I analyzed its complexity. Replacing this with heapq.nlargest() taught me that Python's standard library provides optimized tools for common operations, and understanding when to use them is part of professional development.

### Software Engineering and Database

The Task Management and Inventory Management System enhancements taught me that software engineering is about making deliberate, principled design decisions. When I refactored the Task Management Application from procedural code with global variables to an object-oriented design with proper encapsulation, I learned that OOP is not just a programming paradigm but a way of organizing code that makes it easier to test, maintain, and extend. The decision to separate concerns between the Task class (data) and TaskManager class (operations) reflected an understanding of single responsibility principle that I had read about but not truly internalized.

Working with databases taught me that proper schema design with constraints is as important as the application code. Adding foreign keys, NOT NULL constraints, and CHECK constraints to my Inventory Management System transformed it from a fragile application that could accept invalid data into a robust system with data integrity enforced at the database level. I learned that defense-in-depth—validating data both in application code and database constraints—is the mark of professional development.

### Security

Developing a security mindset has been one of the most valuable outcomes of this capstone experience. When I discovered the SQL injection vulnerabilities in my Inventory Management System, I realized that security vulnerabilities often result from taking shortcuts during development. The original code used string concatenation to build SQL queries because it was faster to write, but this convenience created catastrophic security risks.

Learning to use parameterized queries throughout my application taught me that secure coding practices should be automatic, not afterthoughts. I now understand that every input from users is potentially malicious and must be validated. Every database operation must use parameterized queries. Every constraint must be enforced. This security-first mindset will guide my professional work, ensuring that I build systems that protect user data and resist attacks.

## Portfolio Synthesis

The three artifacts in my ePortfolio work together to demonstrate the full range of my computer science abilities. Each artifact addresses a different aspect of software development while showing consistent growth in code quality, security awareness, and performance optimization.

The **Task Management Application** showcases my software engineering skills through its transformation from procedural code to object-oriented design. The addition of error handling, input validation, and JSON persistence demonstrates my ability to build robust, production-ready applications. This artifact proves I can take a basic working application and enhance it to professional standards.

The **Student Records Management System** demonstrates my understanding of algorithmic principles and data structures. The performance improvements—from 1,000x faster sorting to 10,000x faster searches—show that I can analyze computational complexity and implement solutions that scale efficiently. The inclusion of performance benchmarking demonstrates my commitment to measuring and verifying improvements rather than assuming they work.

The **Inventory Management System** proves my database design skills and security mindset. Eliminating seven SQL injection vulnerabilities shows I can identify critical security flaws and fix them systematically. The addition of foreign keys, constraints, and indexes demonstrates comprehensive understanding of database best practices. The query optimization from Python loops to SQL aggregation shows I understand how to leverage database capabilities efficiently.

Together, these three artifacts demonstrate that I can:
- Design and implement well-structured, maintainable software
- Analyze and improve algorithmic efficiency with measurable results
- Build secure database applications that protect against common attacks
- Communicate technical decisions clearly through documentation
- Reflect on my learning and incorporate feedback into improved work

## Career Readiness

This ePortfolio has prepared me to enter the computer science field with a concrete demonstration of my abilities. When I interview for positions, I can point to specific examples of my work rather than making abstract claims about my skills. I can show employers the code review video where I analyzed my own work critically, the enhanced artifacts with measurable improvements, and the narratives where I reflected on my learning process.

I am particularly proud of the security improvements in my Inventory Management System because security is a critical concern for employers. Being able to demonstrate that I can identify SQL injection vulnerabilities and fix them with parameterized queries shows that I understand real-world security threats. This is the kind of practical skill that employers value highly.

My professional goals are to work as a software developer where I can continue learning and growing while contributing to meaningful projects. I am particularly interested in roles that involve database design and security, as these are areas where I have developed strong skills and genuine interest. I want to work in collaborative environments where code review and knowledge sharing are valued, because I have learned that I do my best work when I can learn from others and help others learn from me.

## Conclusion

The journey through the Computer Science program at Southern New Hampshire University has transformed me from someone who could write code that works into a developer who writes code that is secure, efficient, maintainable, and well-documented. This ePortfolio represents not just the artifacts I have created, but the growth I have experienced as a problem solver, collaborator, and professional.

I have learned that computer science is not just about algorithms and data structures, but about making thoughtful decisions that consider security, performance, maintainability, and user experience. I have learned that good code communicates its intent clearly to other developers and that professional software development requires balancing many competing concerns.

Most importantly, I have learned that I am capable of taking on challenging technical problems, analyzing them systematically, and implementing solutions that make measurable improvements. The confidence I have gained through this capstone experience has prepared me to enter the workforce ready to contribute from day one while continuing to learn and grow throughout my career.

The artifacts in this ePortfolio demonstrate my readiness for professional software development work and my commitment to continuous improvement. I look forward to applying these skills in my career and building on this foundation with real-world experience.

---

**Navigate to my enhanced artifacts:**
- [Software Design & Engineering: Task Management Application](#software-design)
- [Algorithms & Data Structures: Student Records System](#algorithms)
- [Databases: Inventory Management System](#databases)
- [Code Review Video](#code-review)
