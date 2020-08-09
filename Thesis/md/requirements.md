## An overview of requirements

We find e-exams to be advantageous in a variety of ways. Still, e-exams are only valid if they can meet the same requirements that we are asked for in paper based exams. In his book, <Handke> provides suitable requirements. The requirements are limited to topics on which the e-exam software has direct influence (e.g. requirements concerning exam content are not being considered). Further these requirements can be divided into categories:

First, a requirement that defines the desired outcome of the exam:

- **General Validity**. Exams should aim to provide an accurate depiction of an examinees competence level.

Requirements that mainly influence interactions of examinees and examiners with the examination system:

- **Protection against contestation.** No formal, or technical deficiencies should occur that would question the validity of the exam.

- **Equal Treatment.** Individual examinees must be treated equally.

- **Protection against cheating.** Exams must be protected against manipulation of exam outcome by examinees.

- **Transparency.** The examination process and results must be verifiable.

Requirements that mainly influence the technical implementation of how the examination system handles data:

- **Protection of Data.** Data of examinees is personal data, as such it must be protected from misuse.

- **Integrity.** Exam data must maintain consistency, accuracy and trustworthiness throughout its entire lifetime.

- **Attributability.** Taken exams must uniquely map to the examinee and vice versa.

Having identified these requirements, finding the matching design principles is the next step.

### General Validity

Matching design principle: Per question time constraints to allow for partial open book exams.

As the <ETH> states in their paper, examinations should support the purpose of university to produce highly capable individuals. The degree to which students succeed in that aspect is largely based on their performance in exams. Subsequently, students are highly incentivized to focus their studies on the given exam format and questions. This interdependency between knowledge acquisition and examination shows the importance of exam design and poses the question of what and how to test. E-exams enable assessments to more closely depict a students actual skill level by allowing the simultaneous use of multiple question types.

Different question types are particularly well suited to test specific aspects of learning. These questions types can be defined as follows <ETH>:

- **(Semi) Closed questions**, which mainly revolve around the demonstration of _factual knowledge_. Solutions are not disputable, there are only right and wrong answers. Typical formats include multiple choice answers or simple text input. _e.g. "What does *BYOD* stand for?"_

- **Competence questions**, which are suited to test for a certain _practical skill_. Solutions are given in form of an implementation of the specific task at hand. _e.g. "Using the software, implement an e-exam about e-learning."_

- **Essay-type questions**, which are suited for assessing _transfer knowledge_ and understanding. Solutions are given by free text input. _e.g. "Explain why subjects in computer engineering are especially well suited for e-exams."_

Further different degrees of allowed aid can be identified: In open book exams, students are allowed to solve the question at hand using any resource they feel they need. These open book exams rely mostly on both competence and essay-type questions. It could be argued that these types of questions resemble a real world scenario in which access to information is rarely limited. Meanwhile, in such an open book exam situation closed question are rendered insignificant as simple factual knowledge is easily accessible. In order to ask closed questions it is therefore necessary to restrict access to any aid.

Classical paper based exam do not provide a feasible way of combining degrees of allowed aid. Therefore, some question groups tend to be neglected. Resulting in constraints of possibilities to create an accurate depiction of an examinees actual competence. <!-- Look here again -->

With e-exams on the other hand we can implement such a varying degree of usable aid, creating a _partial_ open book exam. This can be achieved by letting students generally use any resource they need in order to answer the question. Additionally, we introduce per question time constraints. These time constraints can be adjusted according to the question type. Leaving closed questions with a harsh time constraint, an _either-you-know-it-or-you-don't_ situation, where there is no time to look up any solution. Essay-type questions just as competence questions can use more generous time frames. Leaving the examinees room to make use of their tools.

Ultimately, examination software in general has no direct impact of what exact questions the examiner asks. The content of questions obviously predefines how good a question can predict an examinees capabilities. Still, with the use of partial open book exams, e-exams allow for a divers question set. Which allows to test factual, transfer and practical knowledge to an equally valid degree.

### Protection against contestation

<!--
Matching desing principles:

- Making the exam offline compatible.

- Caching answers while taking the exam.
-->

Contestation of paper based exams generally is not a common problem. This is mainly due to the controlled environment paper based exams are taken under. Adding, the medium that is used to test examinees (i.e. paper) is fail-safe. E-exams, especially decentralized, ones introduce the possibility of failure of the exam medium. E-exams rely on software, on the operation of the exam device and of course on internet connection.

The most crucial point probably is the reliability of the e-exam software. This high reliability can only be achieved by rigorous testing and continuos improvements. Of course, this applies to almost any software artifact and thus may not be considered a specific design principle per se. Further, device operability largely lays in the responsibility of the device owner. Still, examinees should be advised to keep their devices updated, make sure they are working properly and are plugged into power.

Software wise these directives can be supported by making the exam accessible and workable if the internet connection is lost for short periods of time. Additionally, exam answers should continuously be sent to a server to minimize the possibility of data loss. In case of both a device crash and internet failure, the exam should be persistent on the local storage of the device. The device then can be rebooted and the exam can be continued.

### Equal Treatment

<!--
Matching design principles:

- Providing a cross platform solution.

- Allowing for randomized exam correction.
-->

Equal treatment of examinees should be carried out throughout the entire examination process reaching from taking the exam to the correction of the exam.

Possible inequality arises in some key areas. In BYOD exams student devices are largely heterogeneous, they run different operating systems and consist of different hardware. This fact should not lead to different exam taking experiences. The choice of hardware should be largely irrelevant. Consequentially, it makes little sense to develop proprietary software for each operating system. Modern web technologies provide a common language among different systems. Web applications do not lack speed or functionality and can be adopted cross-platform. The software is hosted at a central instance where it can be maintained and improved and the software artifact is delivered over a modern browser.

The process of correcting exams is also an area where possible inequalities can be found. Especially in paper based exam checking an exam for correctness is one of the most time-consuming processes in conducting an exam. Resulting in fatigue and thus sometimes faults in checking answers. Also, a connection between bad handwriting and worse grades has been found. <James 1927> shows students with bad handwriting get categorically worse grades than students with better handwriting. By using e-exams these inequalities can be fixed. First, some question types, such as multiple choice questions can be checked automatically. This is an immediate improvement over correcting these questions by hand. Second, as exam answers are available in digital text reading and checking answers is easier. Answers must not be deciphered, correction of exams can be done faster. Meanwhile eliminating any biases against certain students.

<!--
Adding, the digital nature of exams makes it possible to give visual aid to the corrector. Automatically highlighting specific terminology can help correctors to faster check students answers.
-->

### Protection against cheating

<!--
Matching design principles:

- Creating a feeling of being survailed.

- Making use of large question pools.

- Randomization of questions.

- Make use of partial open book exams.
-->

When thinking about any assessment the consideration and handling of academic dishonesty (e.g. cheating in an exam) is one of the most important parts. Moving from paper to e-exams poses the questions what parts -- if any -- must be adjusted to accommodate for changed circumstances and environments.

In his paper <McGabe> poses seven fields of possible cheating in exams which he then evaluates by occurrence and perceived severeness. Six of which are relevant for this thesis purpose (The seventh would be _"Using false excuse to delay test taking"_). The fields are can be described as follows:

**Student cooperation**:

- **Knowing the questions.** Learning what is on an exam from someone who has already taken it.
- **Cooperation with outsiders.** Helping someone else cheat on an exam.
- **Cooperation with fellow examinees.** Copying from another student on an exam with their knowledge.

**Use of disallowed aid**:

- **Exploit environmental circumstances.** Copying from another student on an exam without their knowledge.
- **Use of unauthorized crib/cheat notes.** Bringing prepared cheat notes to use in the exam.
- **Use of electronic, unauthorized aid.** Using e.g. a smartphone to google or review lecture material.

Before thinking about how to obviate these cheating scenarios an important statement must be made: Cheating cannot completely be eliminated. There are always ways for students to engage in cheating. E-exams cannot change that. But compared to paper based exams some measures against cheating may be more effective.

**Knowing a question.** As the question finding process in a time-consuming process, a strategy may be to keep questions as secret as possible and reuse them throughout multiple exams. This is a rather ineffective strategy as platforms such as <studydrive> often provide comprehensive protocols from memory of examinees who have engaged in a given exam. E-exams can choose a different approach. Instead of having few questions and keeping them secret, e-exams can leverage large question pools. At a certain point it becomes unfeasible for students to prepare for every available question as question pools grow larger. The digital nature of these questions makes them easily shareable, allowing for larger question pools more quickly.

**Cooperation with examinees.** For closed questions this cooperation can be prevented by using strict time restrictions. As already stated above these questions fall in the category _Either you know the answer or you don't_ there is no need for a lengthy reflection period. As time constraints are tight, there really is no way of communicating with others and solving the question. For more open question types the time limitation is not as tight. At the same time answers require more in depth considerations. To ensure that students write down their own ideas and cannot share their thoughts, the copy and paste functionality can be disabled. Further, e-exams can easily be randomized, thus preventing students form peeking or signaling solutions to each other.

**Cooperation with outsiders.** As decentralized e-exams are not conducted in a controlled environment, cooperation with outsiders becomes a bigger problem. Examinees could try to take the exam in the presence of a more knowing person. Some try to solve this problem by using proctored e-exams. These exams use live surveillance through webcam and microphone that is evaluated by a person watching in real time. This approach hardly scales as for every 4-5 students a supervising proctor is needed. While programs like <ETC Toefl> can make use of such a system, their high test fees leave room for additional expenses. A

Although the live surveillance of students is not a valid option the psychological effects of being monitored can be leveraged. A measure might be to make use of integrated webcams and microphones of the devices at hand. This video and sound data can be reviewed if needed. More importantly it creates a mental barrier. If examinees really commit to engage in academic fraud they will most certainly find a way to do so. The goal is simply to prevent those from cheating that would cheat if they would feel no threat of being caught. The sole existence of any measures makes the students behave more honest. Just as video surveillance makes crime less common at public places <Welsh 2004>.

**Exploit environmental circumstances.** Again randomization can solve this problem. As questions appear in a different order for each student even multiple choice questions can not simply be copied.

**Use of unauthorized cheat notes or electronic aid.** Following the argument made about partial open book exams we find that besides time constraints no additional measures must be enforced. Cheat notes really are not of much help if there is no time to use them.

We find these cheating scenarios to be to a large degree managed by e-exams. Still, as specific software is in use, the degree of cheating must constantly be assessed. Measures against bugs or security flaws must be identified.

### Transparency

The examination process should be transparent for examinees. Examinees must be able to understand their mistakes and shortcomings. This of course implies that the exam software provides ways to give some kind feedback. Second, as examiners are not free of mistakes, corrections can sometimes be faulty. Well implemented transparency allows students to review the examiners correction and possibly contest against single corrections. Important to mention is, that every student should get the chance to review their exam. The digital nature of e-exams makes this degree of transparency easily realizable. Sending a corrected digital copy of an exam, lets examinees review their answers and understand their gaps in knowledge. Contestation against single questions could also be processed in the exam software.

### Attributability, Protection of Data and Integrity

Exam data is highly sensitive and demands high levels of information security. As with any information system, basic information security principles apply. The following points prove to be of special importance.

Exam data must be uniquely traceable to examinees. This can be easily realized by having examinees log into an user account before they can perform any action. Examinees either get a unique identifier in-software or a unique identifier that is provided by the testing authority. Anything they do is then linked to their user id.

To assure solid data protection, strong user rights management must be enacted to assure that only authorized groups can see or correct exams. Data in this way is largely protected from missuses. This measure ties into the integrity of exam data. As access is restricted exam data cannot be changed. To provide even more security answered questions can be sent to a central server instance as soon as students start answering the next question. Further, frequent database backups of the exam data should be standard procedure.

Another consideration to take into account is the availability of the source code. Processes should be completely transparent and comprehensible. Exam authorities should be able to host exams by themselves. This can be achieved by providing the exam providing software in open source format. This has the additional benefit that such software can benefit of crowd participation.