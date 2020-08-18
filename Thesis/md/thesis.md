---
Author: Jasper Anders
fontsize: 11pt
linestretch: 1.5
margin-left: 2.7cm
margin-right: 2cm
margin-top: 3.4cm
margin-bottom: 3.5cm
paper-size: a4
bibliography: ../bib/xm.bib
---

<!--
Tags:

- <cite>: Needs citation
- <!--   : Comment
- <review> : need review
- [!!]: Marked, bad sentence or word
-->

<!-- Taking the current pandemic under consideration, it may not be an option to just move from paper to e-exams. Exams thus must be conducted decentralized, i.d. students take their exams at ho  me. -->

\newpage

# Introduction

The examination process is a large part of education in general. Great amounts of time go into organizational problems and overhead. Although digitizing exams would . A step towards electronic examination would make the process more flexible, scalable and resource-efficient. Meanwhile, leading to a more accurate depiction of a students' competence.

Digitizing exams is no new idea. Although, many concepts [cite papers that talk about byod or multi media room exams] and implementations focus on conducting e-exams in the same environment as _paper-based exam_. Resulting in exams that are either conduced on the universities hardware [@KlausurenAndDerUniMainz]. Alternative the exam is a so called **BYOD** (bring your own device) exam, where the exam taken student owned devices [@GLM2015_RobertPeregoodoff].

With the the current COVID-19 situation decentralizing exam would be of both economical and Technically the

It is important to notice, that _decentralized e-exams_ differ from _paper-based exams_ and even from _centralized e-exams_ in some key points. Foremost, the examiner has less control over the environment the exam is taken under. This raises questions about exam integrity and fairness. These questions must be addressed through careful conceptualization of questions and intelligent software design.

Of course some _e-exam_ are already conducted today. Large proportions are making use of a **proctoring system**. In such a system a supervisor can access the examinees' device, can monitor all their activity and will watch them through their webcam. This proctoring process is costly. It hardly scales and still easily can be fooled.

Further, test-taking applications are found in many _LMS' (Learn Management Systems)_ such as [@Ilias], [@Moodle] or [@Blackboard]. Unfortunately, most often these applications focus on student self-assessment. They also majorly vary in quality and utility. As they are integrated in a complete LMS, changing to the _best_ implementation is in many cases not an option.

Last, as exam data is highly confidential, there is a strong argument to be made against closed source solutions. It is crucial to know exactly how the used application works and how data is handled. Adding, open source projects are less prone to major security issues as the development can leverage the crowd sourcing capabilities that an open source system provides.

# Design oriented research

[@Hevner] proposes guidelines an approach to conduct design-oriented research

1. **Design as an Artifact:** The result of this research project is an IT artifact. It provides an implementation of a specific electronic exam. This artifact aims to be used in the real world examination process.
2. **Problem Relevance:** With the rise of the Corona crisis E-Education suddenly has become a necessity. While there is a wide variety of options when it comes to distributing educational content, there is a shortage of cheap and well-thought-out systems for electronic exams. Even after the Corona crunch, conducting electronic exams has the power to make the assessment process less time and cost intense.
3. **Design Evaluation:** The effectiveness of the artifact was evaluated with particular focus on cheating behaviour. First tests were conducted in a low stakes environment that only some degree can emulate a real test taking environment. Further tests and improvements can be conducted and made in real world exams.
4. **Research Contribution:** There are few systems designed for providing high academic validity (i.d. prevent cheating in exams). Many systems that do exist, make use of _Proctoring_ (the student is continuously watched over video stream) environments which are expensive and still easily can be fooled. This research artifact aims to minimize academic dishonesty through design decisions.
5. **Research Rigor:** This thesis builds upon research in the fields of education. Taking into consideration what other Universities have already incorporated into their examination process and what empirical studies have shown to be valuable and efficient.
6. **Design as a Search Process:**
7. **Research Communication:** This thesis focuses on illustrating design considerations, that were made in order to develop an artifact, that most closely fit the needs of educators. Therefore, this thesis is of interest to those want to build upon the considerations that were proposed. The actual technical intricacies should only briefly be touched upon, to give some insight into the technical base of the given artifact.

# Requirements for E-Exams

We find e-exams to be advantageous in a variety/numerous of ways. Still, e-exams are only valid if they can meet the same requirements that are asked for in paper-based exams. [@Handke2012] provides suitable requirements. These are limited to topics the e-exam software can directly influence, issues concerning exam content are not being considered. These requirements can be divided into three broad categories:

The fist requirement defines the desired outcome of an exam:

- **General Validity.** Exams should aim to provide an accurate depiction of an examinees competence level.

Requirements that mainly influence interactions of examinees and examiners with the examination system:

- **Protection against contestation.** No formal, or technical deficiencies should occur, that would question the validity of the exam.
- **Equal Treatment.** Individual examinees must be treated equally.
- **Protection against cheating.** Exams must be protected against manipulation of the exam outcome by examinees.
- **Transparency.** The examination process and results must be understandable and verifiable.

Requirements that mainly influence the technical implementation of how the examination system handles data:

- **Protection of Data.** Data of examinees is personal data, as such it must be protected from misuse.
- **Integrity.** Exam data must maintain consistency, accuracy and trustworthiness throughout its entire lifetime.
- **Attributability.** One taken exam must uniquely map to one examinee and vice versa.

These categories set a general framework of how to design any examination system. In case of this thesis, e-exams are of interest. They use specific design principles to match the previous requirements. These design principles will be introduced in the following.

## General Validity

As the [@ETH] states in **their** paper, examinations should support the purpose of universities to produce highly capable individuals. The measure of degree to which students succeed in that aspect is largely based on their performance in exams. Subsequently, students are highly incentivized to focus their studies on a exam format and specific question types. This interdependency between knowledge acquisition and examination shows the importance of exam design and poses the question of what and how to test. Different question types are particularly well suited to test specific aspects of learning. These questions types can be define d as follows [@ETH]:

- **(Semi) Closed questions**, which mainly revolve around the demonstration of _factual knowledge_. Solutions are not disputable, there are only right and wrong answers. Typical formats include multiple-choice answers or simple text input. _E.g. "What does *BYOD* stand for?"_
- **Competence questions**, which are suited to test for a certain _practical skill_. Solutions are given in form of an implementation of the specific task at hand. _E.g. "Using the provided software, implement an e-exam about e-learning."_
- **Essay-type questions**, which are suited for assessing _transfer knowledge_ and _understanding_. Solutions are given by free text input. _E.g. "Explain why subjects in computer engineering are especially well suited for e-exams."_

Further, different degrees of allowed aid can be identified: In open book exams, students are allowed to solve the question at hand using any resource they feel they need. These open book exams rely mostly on both competence and essay-type questions. It could be argued that these types of questions resemble a real world scenario in which access to information is rarely limited. Meanwhile, in such open book exam situations, closed question are rendered insignificant as simple factual knowledge is easily accessible. In order to ask closed questions it is therefore necessary to restrict access to any aid.

Classic paper-based exams do not provide a feasible way of combining degrees of allowed aid. Therefore, some question groups tend to be neglected. This constraints possibilities to create an accurate depiction of an examinees actual competence. With e-exams on the other hand, we can implement such a varying degree of usable aid, creating a _partial_ open book exam. This can be achieved by letting students generally use any resource they need in order to answer the question. Additionally, we introduce per question time constraints. These time constraints can be adjusted according to the question and question type. Leaving closed questions with a strict time constraint and creating an _either-you-know-it-or-you-don't_ situation, where the student has no time to look up any solution. Essay-type questions just as competence questions can employ more generous time frames, giving the examinees freedom to make use of their tools.

Ultimately, examination software in general has no direct impact of what exact questions the examiner asks. The content of a question obviously predefines how well this question can predict an examinees' capabilities. Still, the use of a partial open book exams mode allows for a diverse set of question. This mode allows to test factual, transfer and practical knowledge to an equally valid degree.

ADD DESIGN PRINCIPLE

## Protection against contestation

<!--
Matching desing principles:

- Making the exam offline compatible.

- Caching answers while taking the exam.
-->

Generally, contestation of entire paper-based exams is not a common problem. This is mainly due to the controlled environment paper-based exams are taken in. Adding, the medium that is used to test examinees (i.e. paper) is fail-safe. E-exams, especially decentralized ones, introduce the possibility of failure of the exam medium. They rely on software, on the operation of the exam device and of course on internet connection.

The most crucial point is the reliability of the e-exam software. As with any software, high reliability can only be achieved by rigorous testing and continuous improvements. In the end, it is more valuable to have a working system that lacks "quality of life" features than software full of bugs.

Another important point is device operability. Decentralized e-exams are taken on the examinees device.It largely lies within in the responsibility of the device owner to assure it is working as intended. Still, software can assist by advising examinees to keep their devices updated, plugged into power and not to take the exam if they fear device failure.

Software-wise these directives can be supported by making the exam accessible and workable if the internet connection is lost for short periods of time. Additionally, exam answers should continuously be sent to a server to minimize the risk of data loss. In case of both a device crash and internet failure, the exam should persist on the local storage of the device. The device then can be rebooted and the exam can be continued. These measures combined with the fact that modern devices generally show low failure rates assure that the exam environment is fairly save and contestation therefore unlikely.

<!-- The software leaves minimal room for contestaition -->

## Equal Treatment

<!--
Matching design principles:

- Providing a cross platform solution.

- Allowing for randomized exam correction.
-->

Equal treatment of examinees should be ensured throughout the entire examination process, reaching from taking the exam to its correction.

Possible inequality arises in some key areas. In BYOD exams student devices are largely heterogeneous--they run different operating systems and consist of different hardware. This fact should not lead to different exam-taking experiences. The choice of hardware should be largely irrelevant. Consequently, it makes little sense to develop proprietary software for each operating system. Modern web technologies provide a common language among different systems. Web applications do not lack speed or functionality and can be adopted cross-platform. The software is hosted at a central entity where it can be maintained and improved. The software artifact is then delivered via a modern browser.

The process of correcting exams is also an area where possible inequalities can be found.

> **Especially, in paper-based exams checking an exam for correctness is one of the most time-consuming processes in conducting an exam.**

Resulting in fatigue and thus sometimes in answers checking mistakes. Besides accidental mistakes, [@James 1927] has found negative bias in connection with bad handwriting. He found students with bad handwriting get categorically worse grades than students with better handwriting.

By using e-exams these inequalities can be eliminated. First, some question types, such as multiple-choice questions can be checked automatically. This is an immediate improvement over correcting these questions by hand. Second, as exam answers are available in digital text, reading and checking answers is easier. Answers must not be deciphered, correction of exams can be done faster. Meanwhile, e-exams can also eliminate biases against certain students.

<!--
Adding, the digital nature of exams makes it possible to give visual aid to the corrector. Automatically highlighting specific terminology can help correctors to faster check students answers.
-->

## Protection against cheating

<!--
Matching design principles:

- Creating a feeling of being survailed.

- Making use of large question pools.

- Randomization of questions.

- Make use of partial open book exams.
-->

When thinking about any assessment the consideration and handling of academic dishonesty (e.g. cheating in an exam) is one of the most important parts. Moving from paper to e-exams poses the question what parts -- if any -- must be adjusted to accommodate for changed circumstances and environments.

In his paper [@McGabe] poses seven fields of possible cheating in exams which he then evaluates by occurrence and perceived severeness. Six of which are relevant for this thesis' purpose ^(The seventh would be _"Using false excuse to delay test taking"_). The fields can be described as follows:

**Student cooperation**:

- **Knowing the questions.** Learning about the exam content from someone who has already taken it.
- **Cooperation with outsiders.** Reseaving help from someone cheat on an exam.
- **Cooperation with fellow examinees.** Copying from another student during an exam with their knowledge.

**Use of disallowed aid**:

- **Exploit environmental circumstances.** Copying from another student during an exam without their knowledge.
- **Use of unauthorized notes.** Bringing prepared cheat notes to use in the exam.
- **Use of electronic, unauthorized aid.** Using search engines or the lecture material to solve questions.

Before thinking about how to obviate these cheating scenarios an important statement must be made: Cheating cannot completely be eliminated. There are always means for students to engage in cheating. E-exams cannot change that, but compared to paper-based exams some measures against cheating may be more effective.

**Knowing a question.** The generation of questions is a time-consuming process, thus a strategy may be to keep questions as secret as possible and reuse them throughout multiple exams. This is a rather ineffective strategy as platforms such as [@studydrive] often provide comprehensive protocols from memory of examinees who have engaged in a given exam. E-exams can choose a different approach. Instead of having few questions and keeping them secret, e-exams can leverage large question pools. At a certain point it becomes unfeasible for students to prepare for every available question as question pools grow larger. The digital nature of these questions makes them easily shareable, allowing question pools to grow faster.

<!-- loook here again -->

**Cooperation with other examinees.** For closed questions this cooperation can be prevented by using strict time restrictions. As already stated above, these questions fall in the category _either-you-know-the-answer-or-you-don't_ there is no need for a lengthy reflection period. As time constraints are tight, there is no way of communicating with others and solving the question. For more open question types the time limitation is not as tight. At the same time, answers require more in-depth considerations. To ensure that students write down their own ideas and cannot share their thoughts, the input possibilities must be limited. Copying and pasting should be disabled to prevent sharing of answers between students. To further inhibit cheating, e-exams should be be randomized. To allow the randomization to have an effect, navigation between questions should be inhibited, students should not be able to go back and re-answer a question.

**Cooperation with outsiders.** As decentralized e-exams are not conducted in a controlled environment, cooperation with outsiders becomes a severe problem. Examinees could try to take the exam in the presence of an expert. Some try to solve this problem by using proctored e-exams. These exams use live surveillance through webcam and microphone that is evaluated by a person watching in real time. This approach hardly scales as for every 4-5 students a supervising proctor is needed. Programs like [@ETC_Toefl] can make use of such a system, as their high test fees leave room for additional expenses.

Although, live surveillance of students is not a valid option the psychological effects of being monitored can be leveraged. A measure might be to make use of integrated webcams and microphones of the devices at hand. This video and sound data can be reviewed if needed. More importantly, it creates a mental barrier. If examinees really commit to engage in academic fraud they will most certainly find a way to do so. The goal is simply to prevent those from cheating that would only cheat if they would feel no threat of being caught. The sole existence of any measures makes students behave more honest. This can be compared to, surveillance makes crime less common at public places [@Welsh2004].

**Exploit environmental circumstances.** (e.g. Peeking at answers) Again randomization can solve this problem. As questions appear in a different order for each student, even multiple-choice questions cannot simply be copied.

**Use of unauthorized cheat notes or electronic aid.** Following the argument made about partial open book exams we find that besides time constraints no additional measures must be enforced. Cheat notes are redundant if there is no time to use them.

We find E-exam software to be able to enforce measures against cheating.

We find these cheating scenarios to be largely managed by e-exams. Still, as specific software is in use, the degree of cheating must constantly be assessed. Further software bugs must be fixed, while security flaws must be identified and resolved.

## Transparency

The examination process should be transparent for examinees. Students must be able to understand their mistakes and shortcomings. This implies that the exam software provides ways to give feedback. Further, as examiners are not free of mistakes, corrections can sometimes be faulty. Well implemented transparency allows students to review the examiners correction and contest against individual corrections. Important to mention is, that every student should get the chance to review their exam. The digital nature of e-exams makes this degree of transparency easy to realize. Sharing a corrected digital copy of an exam, allows examinees review their answers and understand their gaps in knowledge. Contestation against certain questions could also be processed within the exam software.

## Attributability, Protection of Data and Integrity

Exam data is highly sensitive and demands high levels of information security. As with any information system, basic information security principles apply. The following points prove to be of special importance.

Exam data must be uniquely traceable to examinees. This can be easily realized by having examinees log into an user account before they can perform any action. Examinees either get an unique identifier in-software or an unique identifier that is provided by the testing authority. Any of their actions is then linked to their user id.

To assure solid data protection, strong user rights management must be enacted. This guarantees that only authorized groups can view or correct exams. In this way data is largely protected from missuses.

<!-- Das hier ist einfach noch schlecht! Ist aber ein punkt für integrity and data prot-->

This measure ties into the integrity of exam data. As access is restricted exam data cannot be changed. To provide even more security, answered questions can be sent to a central server instance as soon as students continue to the next question. Further, frequent database backups of the exam data should be standard procedure.

Another consideration to take into account is the availability of the source code. Processes should be completely transparent and comprehensible. Exam authorities should be able to host exams <!-- exams? Software --> . This can be achieved by providing the exam software in open source format. Further open source programs can leverage crowd participation to render software bug-free and to eliminate existing security flaws.

\newpage

# Software

In the previous section I laid the requirements an artefact must match in order to provide a appropriate exam software. Internationally there exist many testing tools. In this thesis we will evaluate five different software alternatives:

- [@Ilias]
- [@Moodle]
- [@OpenOlat]
- [@Blackboard]
- [@LPlus]

These five systems are chosen because they consist of popular e-learning applications in use by large parts of german higher education. Illias, Moodle and Open Olat are open source and free to use. Both Blackboard and LPlus are closed source and are paid products. Besides LPlus are all of them full LMS (learn management systems). Such learn management systems provide management of the complete e-learning process in one application. LMS allow for distribution of material, student exchange and provide a platform for educators to get in touch with their students. These systems also allow for way of assessing students. As universities in german higher often already have such LMS operative, using the integrated assessment tools becomes a seamless experience. While this sounds great in theory, the integrated assessment tools often lack in features or quality.

I will measure the quality of all five tools based on their degree of fulfillment of the requirements I layed out earlier. As a baseline all these tool fulfil some of the specifications to the same degree and in the same way.

All of them have user management with a respective permissions. Further, all of them rely on a browser to provide their services, thus being device agnostic and matching _the equal treatment requirement_.

## General validity

As a starting point, all products allow a variaty of question types. Matching the first design principle. To completely match the _general validity requriremen_ exams need to be able to enforce per question time constrains. Here only [@OpenOlat] and [@LPlus] can provide such a feature. The other systems allow for time constraints set on the whole exam, time limits on a question base is not possible.

## Protection against contestation

One of the biggest shortcomings of the softwares at hand is their way of handling connection errors. All of them rely on a stable internet connection. Loosing connection forces the student to wait until the connection is reestablished. This is especially problematic with questions that rely on time restrictions. As with local storage of answers, also timestamps can be saved. This assures the timely answering of questions. Students then could directly move on to answer the next question. Due to the lack of any offline capabilities, a students answers could be lost. Not providing a student with an adequate way of solving an exam this could lead to contestation.

## Transparency

In terms of transparency LPlus, OpenOlat and Moodle perform well. They provide a way of giving feedback to specific questions. Students can review their exam results together with this feedback. Still, direct contestation of corrections is not possible in app, making this process fallback on other means of communication. Ilias and BlackBoard provide no way of get any feedback beside the achived points in a given question.

## Protection against cheating

As we have seen above only LPlus and OpenOlat provide a way of creating partial open book exams. Time restrictions are a main tool for restriction of several ways of cheating. Exams created with Ilias, Blackboard and Moodle thus can only rely on a subset of the possible question types or they risk cheating.

None of the systems provide a way to do visual or auditory supervision. Students identities are in no way checked. These systems thus open up possibilities of students either getting help from outsiders or outsiders completely taking the exam on their own.

Another part where no measures are taken is in the restriction of input. None of the products allows for any restriction in input.

Further, exams must be customizable in such a way, that students cannot jump between questions, cannot re-answer questions and can only see one question at a the time. This customization is found in Moodle, LPlus and OpenOlat. Both Ilias and Blackboard are very limited in that regard.

Lastly, all tools allow for a random order for questions in an exam to appear in. Also every tool provides a way of creating and maintaining a question pool. Questions also can be imported and exported, theoretically allowing for sharing between examiners. To allow for truly large question pools in reality sharing at a platform magnitude must be envisioned. Non of the products can provide such a platform.

## Protection of Data, Attributability and Integrity

With respect to _Protection of Data, Attributability and Integrity_ all solutions provide user management with different roles and permissions. Adding all of the products are still actively developed and thus contiguously improved.

<!-- - A way to im-/export question and to manage question pools.
- A way to implement all common question types.
- A way to automatically grade closed questions.
- A way to randomize the order of exam questions.
- A in depth documentation and/or community.
- Finished exams can be collected remotely.
- Exam data is stored at a central instance and can be accessed remotely.
- Examination is not bound to a singe location and issued over browser. -->

## Further considerations

As already mentioned above most of the systems currently in use are LMS. As we showed above, they not fulfil all the requirements needed for an exam. Problematically, due to their heavy integration with every part of an universities systems, LMS are not easily swapped out. Instead, it may be advantageous to use a standalone solution that uniquely focuses on providing e-exams.

\newpage

# Designing the software artefact

In the previous chapter we found no exam software fully matching all requirements. In the following an overview of how a software artefact could implement all these design principle from a technical point of view will be made. Further, as a proof of concept two design principles are implemented in a working software prototype. This prototype helps determine software architecture as well as used technologies. First, general thoughts about data structure will be made, followed by an short introduction into used technologies. All these statements will be made with the exam requirements in mind.

As mentioned earlier open source code can allow for a more secure and transparent software. Consequentially the source code of this artefact can be found on github under the MIT open code licence^([@https://github.com/jasperanders/XM], [@https://github.com/jasperanders/XM-Api])

## Data structure and architecture

The artefact is classic client-server application. With a frontend (client), responsible for interaction with both examinees and examiners and a backend (server), responsible for data handling. The backend server runs on a [@Node.js] server, while the frontend is delivered via any modern browser, thus fulfilling the _equal treatment requirement_.

The client and server side communicate over a simple REST API. The advantage of a client-server application lays in the separation of the data and the end-user. Users do not have direct access to data but any read or write action must be made over and API. Here permissions can be checked and possible misuse inhibited. Second, as the user has no direct influence on the servers actions the sever can act as a source of truth. Data that was once committed to the server is now immutable. For example, the foraging of exam answers after submission becomes impossible. The API can also provide different kinds of endpoints to interact with for different kinds of users. Examiners for example can use one API endpoint to create exam questions, whereas students will get an error code if they try to interact with it.

One of the most important design considerations is the data model that is used to store and access exam and user data. There are four central instances:
First, there is the question instance. This is probably the most important instance. Especially with the creation of question-pools in mind, it is clear that question instance must live independent of any exam. A question consists of a title, the question type, the question text, the questions points and the questions time limit. Further each question has a question body, the shape of the question-body depends on the question type. For example the multiple-choice question-body consists of a reference to the question it belongs to and a selection of possible answers. For free-text questions currently no additional body is need, still to be consistent in data structure and to allow for later additions, free-text questions also have a body.

These questions can then be assembled into exams. Each exam contains an exam name users that are allowed to take part in a given exam and an exam date. Most impotently, an exam contains an Array of question ids, which constitute the exam content.

The third central instance is the user. Users can either be examinees or students with each having different roles. Students for example can not create exams or questions. Examiners on the other hand can do so. If any new data instance is create, e.g. a new question, the author automatically is set to the logged in user, creating the given instance. Further, users posses an email and password, a name and a unique identifier. This id is provided by the application but could also be an identifier provided by the testing authority. With user handling and automatic assignment of authorship we can assure the _attributability requirement_ and to a large degree the _protection of data_ and the _integrity requirements_.

The last key instance is the answer. For each question an examinee answers an answer instance is created. This instance contains a timestamp at which the question is started, a timestamp at which the question was answered and the question-id the answer is referring to. Additionally the answer object provides a flag that marks it as an master answer. Master answers are the correct answers, or in case of free-text questions provide a guideline of what is to be considered correct. Analogue to the question, the answer also bears an answer-body. This form of this body again is dependent on the question type. Multiple-choice question-body contain the selected answers, whereas a free-text question-body contains the given free-text answer. Additionally, any answer body contains a reference to the answer and to the fitting question via their respective ids.

The above provides an overview of the data structure as found in the database. As this app inhibits offline capabilities large portions of the above data structure can be again found in the frontend application. Of course the data is reduced to the data user, e.g a student, is allowed to see but references among question and answer remain identical. To realize the above mentioned offline capabilities the exam data is at all times persisted in the local storage of the browser. Data remains in this local storage until deleted by the app or intentionally removed by the user. If there is an internet connection the data in local storage and the data in the local storage remain the same. Should internet connection fail, will the exam continue as normal. Answers will be saved to local storage and at a later point in time sent to the server.

Depending on the circumstances students are taking their exams, examiners can adjust the degree of offline capabilities. Students could be allowed to take their complete exam in offline mode and only at the last question should sent their answers in. Alternatively students could be allowed to only have connection failures of a single question. With the handling of offline capabilities we can assure the _protection against contestation requirement_.

To provide a way to meet the requirement of **general validity**, and to fulfill parts of the design principles to assure **protection against cheating**, the frontend application must enforce per question time constraints. While the backend can review the actual used time the user interface must assist the student in taking as much time as they are allowed. The artefact achieves this by showing the remaining time and submitting the currently provided answer. This answer is then sent to the server. Students are thus forced to comply to respective time constraints, leaving them no room to accidentally miss allowed times.

## Tech Stack

Both the server and the client side are written in a code language called JavaScript. It is the most popular language on [@Github https://octoverse.github.com/#top-languages]. JavaScript allows programmers to realize the complete technology stack with one language, making it a compelling language to write an application in. Besides many modern and popular libraries for web development are written in JavaScript. Some of these libraries also find use in this artefact, the most crucial being [@React] and [@Express].

[@React] is "a JavaScript library for building user interfaces". It uses structures that are devidable in reusable components. React makes it easy to create complex application instead of only simple websites. It was orignally created by [@Facebook] and finds it use in the tech-stacks of [@Uber], [@Airbnb], [@Netflix] and many more. Further the frontend uses the JavaScript superset TypeScript. TypeScript allows to define and check for complex types whereas JavaScript in general is typless. These types allow for more secure data handling making the application overall less prone to bugs. Lastly a ui-library is used to create a visually more pleasing experience faster.

[@Express] is a common library to create backend services with. It is lightweight and allows for the creation of both simple and complex APIs. As many backend-applications rely on the same structure generators for the common fundamentals exist. For this artefact I used the [@JonasScholz] Rest API generator. The express server also handles data storage, for this purpose a database is connected. The artefact uses a noSQL database called [@MongoDB]. [@MongoDB] does not store data in tables but in JSON like documents. As the JSON format is inspired by JavaScripts objects, the data structure used in the frontend part of the application thus directly translates to the data structure that is used to store the given data.

## Future implementations

As the artefact is only a proof of concept and no market ready software it lacks some key features. Exams for example can be taken but there is no way of evaluating them through a user interface. As the correction of exam is not implemented at the moment the _transparency requirement_ remains unmatched at the current state of the artefact.

Further the the video and sound surveillance is not an implemented feature jet. Protection against cheating thus remains also partially unmatched. As can be seen above, the video supervision only addresses the aspect of cheating by the use of outsider help. Looking at the design principle list, this supervision of students is the only measure against cheating that is not enforced.

A design principle mentioned is the usage of large question pools. In theory is there a way of creating such a question pool in the current software artefact, still there are some limitations. To really generate large question pools, the power of large groups must be utilitized. Universities have created questions for numerous years but as questions leak or get published, these questions remain worthless for a single institution. Sharing them on the other hand opens questions up to new uses. To really enable the common sharing of questions two things must be achieved. First a common question format must be found. As question layout and design should be handled by the application the question is used in this standard should only contain data and no markup. The data structure of the question type of this artefact could theoretically serve such a purpose. Still, the data structure must firmly be evaluated and surely extended. Second a platform is needed to share questions. Such a platform should also take care some kind of quality assurance. At the time of this writing such a platform does simply not exist.

Lastly a note about usability and complexity of the artefact must be made. As this artefact serves as a minimal viable product, many of the user interactions are not suited for large amounts of data. Regarding the further development of the app usability and performance must continuously be evaluated and incrementally improved.

<!--

================================================================================

**General Validity.** Open Book exams.
**Protection against contestation.** Offline Capable open source
**Equal Treatment.**  via Browser.
- **Protection against cheating.** open book, video and sound survaillance.
- **Transparency.** a way to give feedback, sent corrected feedback directly to students
- **Protection of Data.** User Rights.
- **Integrity.** Exam data must maintain consistency, accuracy and trustworthiness throughout its entire lifetime.
- **Attributability.** One taken exam must uniquely map to one examinee and vice versa.

================================================================================

## The case for e-exams

E-education is a much discussed topic. Most of the educational material has become digital. Still, paper-based exams are the way to go, when it comes to assessments in German higher education. Altought some universities amonge these are the FU Berlin and the Johannes Gutenberg University Mainz have implemented some way of e-assessment, it still lacks wide application.

In its research question this thesis ask about how to imporve upon centralized e-exams. This implies, that e-exams in general are superior to paper-based exams. There is good reason for this implication. It is a good idea to take a look at these reasons before moving on.

### Why move from paper based to electronic exams in the first place? inherented vs. earned advantages

<!--
Section overview:

- paper-based exams are still the way to go
- why do we want BOYD and what is it
- who else is using it?

- !what is an e-exam in the first palce
- !technical requirements of a systems. i.d. Browser -> Moodle/Blackboard...
-->
<!--
Put simply central e-exams replace the pen and paper of paper-based exams with a computer or tablet. To give intuition of the advantage of e-exams i will focus on _bring-your-own-device_ (BYOD) e-exams. In BYOD exams the device the student is taking the exam on is not provided by the universiyt authority, students bring their own tablet or laptop to take the exam on. The BYOD concept is not new. For example Robert Peregoodof talked about the BYOD implementation of the University of British Columbia in the <Glm> conference.

It is important to note that moving from paper-based exams to e-exams should be a strict uprgrade. Still, paper-based exams and e-exams are different in some key points. Some things that were considerated best practice must be reevaluated and rethought in order to adequately fit the e-exam context. As I will show these changes do not limit the examination process but rather improve it.

When compared to paper-based exams e-exams provide many advantages as [@Handke2012] disscusses in their book. I will devide these into two different types. The fist type are inheren t advantages. These are advantages that arise from soley digitizing a paper-based exam. These adavantages mainly effect the efficiency of the assessment process.

The other type of advantages are created through additional considerations and by rethinking how paper-based exams approach the examination process. These advantages arise mainly from improvements in testing accuracy and equality.

In order to later assess the quality of existing software solutions, after each section I will derive requirements. These requirements are needed to make use of the theoretical advantage.

<!--
As I want to give intuition, why moving to a _decentralized_ e-examination system might be benificial, I will not discuss other ways of realizing central e-exams then the _bring-your-own-device_ (BYOD) approach.
-->
<!--
### Exams as a logistics problem

<!--
Is this really the first thing that i talk about?

- Exams can be corrected remotely
- Exams can be archived faster an more securely
- Less people move
- Exams can be reviewd remotely

-->
<!--
Thinking about the inherent advantages of e-exams, the logistical implications of exams pop into mind. To illustrate this we use the examination process at the KIT as an example <cite>. Although some steps may differ from university to university, the gist remains.


Exams must be printed and stapled. As, exam taking students are numerous, it is common for exams to take place at many different sites. Therefore, on the test day exams must be carried out to the test site. Here, the Ciw of the KIT <KlausDurch> recommends at least two supervisors per test site. On test site, exams must be distributed to students. After the exam is written, exams are collected and counted. They are then carried back to a central location, where they remain until correction. For answer checking, correctors come together, again at a central location, where they then are able to correct the exam. After correction a grade for students is published via internet. Succeeding, an exam revision for students is planned and executed. Lastly exams are archived in their paper form.

It is not supprising that handeling large amounts of paper results in logistics overhead. Removing the paper, subsequentially removes much of the logistics overhead. In an e-exam all of the exam data is digital. There is no printing, since exams are directly transferred to the students device. Further stundets answers can automatically be retrieved after the exam is over. Exam answers are digitally available. The correction of answers is no longer bound to a certain site but can be done remotely. Exam results and feedback can be directly issued to the students. Thus, revision can also be realized decentrally. The digital exam data can then be easly archived.

This comparison illustrates the advantage of e-exams with regard to logistics. Not only is there less movement of employees but more importantly there is no movement of physical paper. Further we find advantages in the digital archiving. Data can be stored space efficiantly with no need for large physical archives. Adding, archives are much saver as redundant backups are feasable and cheap.

**Requirements:**

- Finished exams can be collected remotely.
- Exam data is stored at a central instance and can be accessed remotely.
- Exam data can be arcived.

### Statistics on the fly

Thinking of the digital nature of exam data another advantage emerges. The digital nature of e-exams allow for a fast creation of statistics. Whereas in paper exams every piece of information must be manually digitized, e-exams are digital out of the box. Thus, analasys of exams becomes more feasible. Thinkable are statistics about general performance, but also analasys of specific questions, or student groups. As the exam is the sole indicator of a students understanding of the matter at hand, it is of utmost importance to understand where students struggle and what they are capabil of. Having easy access to exam data yields the possibility of both better exams and better courses.

**Requirements:**

- Possibility to create a statiscs automatically.

### Questionpools

<!--
Stupid name.

- Show power of collaboration im question pools. <cite>
- Students can fill your question pool.
- exam question must not be treated as sectets any more
- ? a social network for question sharing??
- refer to open source as model


Part of the complexity and time intensiveness of exam creation lays in creating appropriate questions. Although many courses are not unique to one university, sharing of test question is not common. In paperbased exams there are no standards and there is no suitable collaboration platform. In paper-based examination there is no real foundation for sharing and reusing exam questions.

E-exams have to make use of an software artifact in oder to leverage their theoretical benefits. Such a artifact allows for an enforcment of a shareable general format. If users create exams in a specific software, implementing a standard is fairly straight foreward.

> Such a standard already exits under the name of <QTI 2.2>. Having a standard allowes for educators to collaborate to create exams.

Further this collaboration must not be limited by a singel exam with only a few questions. Exams can come from question pools --- a small subset of questions is selected from a way larger superset. The development and maintenance of a large question pool is very time intensive for a single person, that is why collaboration is so important. Projects in open source software show how collaboration of many can function with great success.

Large question pools do not only help in exam creation, as they allow to produce exams automatically, it also prevents students from knowing the exam beforhand. This will be further ellaborated in the section about cheating.

**Requirements:**

- The exam software allows for management of question pools.
- The exam software allows for export of questions, ideally for in a sharable format.

<!--
Often exam questions are treated as secrets as they are used again and again. This secrecy can not relyably be enforced. It is genral procedure that students collaborate to create in depth Gedächnisprotokolle <cite>, which are then uploaded for public access. Having a large question pool, makes it almost impossible for a student to prepare all questions beforehand, creating a more sound depiction of the students skillset.

As the Zurich University has proposed a general Format for e-exams <cite>, these exam questions are now easily shared among colleges and other universities. These questions can then be collected in so named question pools. At a point where a question pool is large enough, exams can be randomly generated using the exams [!already present in the pool!]. Instead of conceptualizing new exam questions, only the question pool must be taken care of.

Some scholars such as [@Handke2012] have concerns about filling such a question pool <cite>. If this had to be done by one examiner, alone this would really be a serious task but in times of wide spread social media sharing questions or entire pools is worth consideration. As a other way of filling question pools, questions could be thought out by students as exam preperation. Filling the question pool may seem like a daunting task, but making utility of crowd thinking and past experiences can dramatically help this endavour.

Here e-exams show their capabilies in network effects. As more examiners and universities use e-exams, more questions are generated for sharing. Being capable to make use of social media like structures would really help everybody to generate high quality exams fast. As many would argue, it is easier to review an already good selection of questions and pick good ones than to rethink them all from scratch. [!At the moment no sturcture exists which makes use of such ideas...!]
-->

<!-- ### Partial Open Book Exams -->

<!--
TODO:
- Bullemie lernen

Moving beyond time and efficiancy improvements.
- Fair depiction of skill
- introduction into open book exams
-->

<!-- **Requirements:**

- Exams must allow for singe question time restrictions.
- Question access must be restricted after answering the question.
- Questions must be displayable one at a time. -->

<!--
These partial open book exams can be realized through time constraints. E-exams can thus provide an environment that resembles real world problems more closely.

Open Book exams depict skills in _high order cognitive processes_ <Krathwohl> way better as they resemble real world scenarios more closely.

Additionally through per question time contostraints closed tasks formats that mainly test for fact knowledge can be implemented. Resulting in partial open book exams.

As e-exams allow easy and equal access to numerous additional resources (i.e. via internet) they make open book exams more feasable.

Seeing exams as an incentive to prepare for reallife problems, it is only sensable to pose questions that resemble reallife problems. Real life problems do not ask for facts but for application and connection of knowledge.

In an exam implementation questions that test for fact knowledge can be seen as closed or semiclosed task formats <ETH>, tasks that rely more strongly on.

Thinking about skillsets reveals another problem of paper-based exams. As many have stated, exams often fail to depict real life problems <cite>.

In contrast to exams, real life almost never asks soley for facts, it asks for a brought application of knowledge. It asks for problem solutions, no matter the resource . There is a case to be made to test for fragestellungen <cite>, that come up in real life in order to fairly get a students skill level. When trying to achive this, open book exams may come closest to depicting a real life problem situation <cite>. On the other hand some fact knowledge is of utmost importance <cite>.

[!E-exams on the other hand can provide a mixture of both <cite>.  Consider an exam where in principle every resource could be used. In such an open book exam especially transfer knowledge can easily be tested. As we discussed fact knowledge is also essential part of the examination process. As this fact knowledge, in a real world application must be available in seconds it is only a reasonable thing to just enforce a time restriction to any fact questions.

In this way e-exams can achive a hybrid testing form. It allowes examiners to more reallistically assess a students real capabilities. Moving educational assessments  closer to real world requirements. This also helps to steuer against the trend of Bullemie lernen <cite>. As studendts find themselves forced to wiedergeben sometimes hundereds of pages of scripts, this short term memory is reinforced.

> > E-exams must allow for partial open book exams.

- [ ] Question types!
 -->

<!-- ### Cheating and randomization -->

<!--
As <cite> found in his paper there are two main categories when it comes to cheating. Planned and spontaineous cheating. Spontainous cheating accures in stress situations where the student feels overwehlmed. It may include looking at other students worksheets or [!even going to the toilet!] to look something up on the internet. Planned cheating on the other hand is intended by the stundet beforhand. The student deposits a cheat sheet in the bathroom, or directly to the exam. Even if the Folgen of cheating are in most cases a failure of the exam, cheating is still common among students. A study of ... found that measures against cheating had almost no effect <cite>.

We must keep this in mind when thinking about e-exams. Against spontaious cheating, some measure can easily be enforced. As tests can be highly randomized looking at a neighbours screen may lead to no new information.

Otherwise, as in a this first step we just replaced paper with a computer there are basically the same eforcements possible. Software such as the open source safe exam browser of the ETH Zürich (link) can be used to make other programs on the device inaccessible during the exam <cite>. So in theory e-exams can be just as safe as paper-based exams. In his paper <cite> found that many cheating methods in e-exams can be circumvised by simple measures.

As I discussed earlyer cheating may not even be a big concern if exams rely on (partial) open book. Open book exams do not need restriction of resources. For an open book exam not even software has to be restricted on students devices. This has also the benefit, that such a system has less parts that must be maintained, thus being less prone to errors.


## From central to decentral e-exams

In the previous section I talked about advantages of central e-exams compared to paper-based exam. One key characteristic of e-exams is that they are issued via the internet. We can use this to remove any local component of e-exams, thus making them decentalized. In the following, I will talk about advantages that decentral e-exams bare and the implications of decentralizing exams on cheating and infrastructural considerations.

### E-Exams as an logistics problem

<!-- find source to proove its a problem
As seen above, e-exams can be immensely more efficient in terms of logistics, compared to a paper-based exam. There are however still some shortcomings. First, consider the allocation of students to their respective test taking location. As different students take part in different exams this allocation grows ever more complex and requires lots of planning of a central authority. <!-- Look at software for proof  Making e-exams decentral allows for this process to be streamlined enourmously.

Second, for supervision of exams human resources are needed. The <KIT> for example recommends two supervisors per location. E-exams can free up some of these resources. To do this we need to take earlier considerations about partial open book exams into account. As I layed out, Partial open book exams allow for tests that do not ask for supervision, making existing supervison obsolete.

When talking about decentralizing e-exams I think it is important to say that the goal is not to force students to write their exams at home. There still can be space reserved for exams by the university. The managemant and supervision of these spaces just becomes magnitudes more easy.

**Requirements:**

- Examination is not bound to a singe location.

### Cheating

<!--
We already discussed the need for local storage above. Earlier we takeld about it as a measure against data loss in event of a connection error. Moving e-exams into the decentralized realm poses the need for encrypted storage of data. As data is send from the local storage tempering with the data must be prevented at all cost.
-->

<!-- ### Infrastructure -->

<!--
## Problems


This section cannot be called problems! Maybe Worries?

- What problems are there why are they wrong.
- change management/being afraid of new tools

As I have show above e-exams bare many theoratical advantages over paper-based exams. In reality these advantages can only be realized through fitting software.

Many <cite> have pointed at problems that may arise from switchig from paper-based exams to e-exams. Some of these problems are not of any concern as techincal advancements have made them obsolete.

<cite> have talked in their paper about the provision of technical infrastructure. They pose a question about the utility and scale of such a infrastukture. As the [paper] aged the techinical sircumstances changed, nowadays it is almost universal for students to have access to a webbrowser <!-- why a web browser? see section about technical requirements  . And really thats all they need. Although not recommended, exams could really be taken on any smartphone. <!-- good gist. bad writing.

Another concern touches upon connection problems <cite>. There is no doubt upon e-exam using a client--server structure <!-- technical requ. . Dependant on the implementation, this may make e-exams prone to connection errors. For example if after every question a new question must be fetched from the server having connection errors can quickly ruin the exam for anyone that is taking it.

> Req: e-exams must sustain in unreliable connection environments

<!-- this has to come in the solution part.  the other hand there is the possibility to store the exam and the given answers in the local storage of the browser. As long as the browser is not reinstalled or forced to clear its chache the exam information is secure. To prevent fiddelling with the local chache it could be encrypted. Using this method e-exams could be counducted even be conducted offline, only to send in the exams solution and to download the exam questions an internet connection would be needed. Of course such a soulution must be tested firmly to make sure that any way of hacking the exam is prevented.
With regard to the configuration and usage of an e-exam tool, it is clear that a soulution that is easily usable for novice users but yields potential for more advanced users is of utmost importance. <!-- only problems, not solutions Examiners must have the chance to learn the new tool, ideally this is supported by the usage of hight standards of user interface design.


Politics and angst also play into the above problems. As new technologie and software often creates a sense of being overwhelmed there must be a strone emphasis on showing examiners the advantages an e-examination system could give them. E-exams especially show their potential when being widely adopted. As more usage of e-exams can lead to network effects. Especially inside an institution there must be enforcement of the usage of new systems. The faster a new way of working gets adapedt the faster it can improve. In this way also small exams are very valuable. It is even thinkable to get immediate feedback of the examinees to improve the system or to get a students feelings about the exam. As the examination infrastructure is easily scalable, there is not need for smaller exam groups to move back to paper. Questions and questionpools can be created in the same way as for bigger exams and as a new e-exam does not need more resources there is no need to hold back.

======================================= <!-- TODO: Bis hier!!

## Bonus

University as a way to help you gain knowledge not a way to test it.

## Moving beyond the limits of education

Education really is a problem of scale. Many studies have shown that the big inequalities that we see today in part are enabled by inequalities in education. Through an open education program many universities aim to dwarf this inequality. The biggest parts of the universities education are: Lectures, tutorials and exams. Today already you can view some of the best lectures online, for free. As Harvard takes part in a open education program. Second, through the rise of plattforms such as the stackexchange stack tutorials have become somewhat crowdsolved. Finding a solution to broughtly test students no matter their location would make a enormous step in the right direction.

## Change and scale

<!-- This is not really of interest.

Some scolars express concerns about the infrastructural scalability of e-exam systems. In their eyes, exams only provide utility with X students or more being part of the exam. This argument ignores the scaleable nature of the an exam system. Moving to e-exams must not be a decision of one course or one Lehrstuhl alone.

- [ ] Größe von e-exams

## Making the move seamless

As briefly touched upon, e-exams must be at least as comfortable as their paper based counterpart. This especially is important when we think about nature of e-exams. As e-exams rely in a client server model they also rely on internet connection.

## Freeing up resources

## Democratic exam dates

 -->
