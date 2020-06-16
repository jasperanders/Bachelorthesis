---
Author: Jasper Anders
---

# Which requirements need to be matched to allow for sound capability testing, in form of decentralized e-exams?

<!--
Tags:

- <cite>: Needs citation
- <!--   : Comment
- <review> : need review
- [!!]: Marked, bad sentence or word
-->

## Introduction

The examination process is often a **tedious task** for those who are in charge. Great amounts of time go into organizational problems. Digitizing exams would resolve many of these problems. A step towards electronic examination would make the process more flexible, scalable and resource-efficient. Meanwhile, leading to a more accurate depiction of a students' competence.

Taking the current pandemic under consideration, it may not be an option to just move from paper to e-exams. Exams thus must be conducted decentralized, i.d. students take their exams at home.

It is important to notice, that _Decentralized E-exams (DE-exams)_ differ from _paper based exams (PB-exams)_ and even from _centralized e-exams (CE-exams)_ in some key points. Foremost, the examiner has less control over the environment the exam is taken under. This raises questions about exam integrity and fairness. These questions must be addressed through careful conceptualization of questions and intelligent [software] design.

Digitizing exams is no new idea. Although, most concepts and implementations focus on conducting e-exams in the same environment as _PB-exams_. With regard to COVID-19 this is not an option. Of course some _DE-exams_ are **already conducted** today. These exams are, for the most part, making use of a **proctoring system**. In such a system a supervisor can access the examinees' device, can monitor all their activity and will watch them through their webcam. This proctoring process is costly. It hardly scales and still easily can be fooled.
Further, test-taking applications are found in many _LMS' (Learn Management Systems)_ such as Ilias, Moodle or Blackboard. Unfortunately, most often these applications focus on student self-assessment. They also majorly **vary in quality and utility**. As they are integrated in a complete LMS, changing to the _best_ implementation is in many cases not an option.
Last, as exam data is **highly confidential**, there is a strong argument to be made against closed source solutions. It is crucial to know exactly how the used application works and how data is handled. Adding, open source projects are less prone to major security issues as the development can leverage the crowdsourcing capabilities that an open source system provides.

### An overview of criteria and derived questions

The main criteria emerge as:

- The electronic examination process must be advantageous compared to paper based examination.
- The exam has to have a high level of integrity. Students cannot fake their identity, cheat, cooperate, use disallowed aid or access exam questions beforehand.
- The exam questions must aim to fairly extract a students' skill level.
- Students must be treated equally in the answer checking process.
- The e-exam taking process must be at least be as stress-free as the paper base equivalent.

Having identified these main criteria, I will ask _sub-research questions_ on how to meet these criteria. In doing this I will give insight into how other systems perform.

## The case for e-exams

E-education is a much discussed topic. Most of the educational material has become digital. Still, paper based exams are the way to go, when it comes to assessments in German higher education. Altought some universities amonge these are the FU Berlin and the Johannes Gutenberg University Mainz have implemented some way of e-assessment, it still lacks wide application.

In its research question this thesis ask about how to imporve upon centralized e-exams. This implies, that e-exams in general are superior to paper based exams. There is good reason for this implication. It is a good idea to take a look at these reasons before moving on.

### Why move from paper based to electronic exams in the first place? inherented vs. earned advantages

<!--
Section overview:

- paper based exams are still the way to go
- why do we want BOYD and what is it
- who else is using it?

- !what is an e-exam in the first palce
- !technical requirements of a systems. i.d. Browser -> Moodle/Blackboard...
-->

Put simply central e-exams replace the pen and paper of paper based exams with a computer or tablet. To give intuition of the advantage of e-exams i will focus on _bring-your-own-device_ (BYOD) e-exams. In BYOD exams the device the student is taking the exam on is not provided by the universiyt authority, students bring their own tablet or laptop to take the exam on. The BYOD concept is not new. For example Robert Peregoodof talked about the BYOD implementation of the University of British Columbia in the <Glm> conference.

It is important to note that moving from paper based exams to e-exams should be a strict uprgrade. Still, paper based exams and e-exams are different in some key points. Some things that were considerated best practice must be reevaluated and rethought in order to adequately fit the e-exam context. As I will show these changes do not limit the examination process but rather improve it.

When compared to paper based exams e-exams provide many advantages as <Handke> disscusses in their book. I will devide these into two different types. The fist type are inherent advantages. These are advantages that arise from soley digitizing a paper based exam. These adavantages mainly effect the efficiency of the assessment process.

The other type of advantages are created through additional considerations and by rethinking how paper based exams approach the examination process. These advantages arise mainly from improvements in testing accuracy and equality.

In order to later assess the quality of existing software solutions, after each section I will derive requirements. These requirements are needed to make use of the theoretical advantage.

<!--
As I want to give intuition, why moving to a _decentralized_ e-examination system might be benificial, I will not discuss other ways of realizing central e-exams then the _bring-your-own-device_ (BYOD) approach.
-->

### Exams as a logistics problem

<!--
Is this really the first thing that i talk about?

- Exams can be corrected remotely
- Exams can be archived faster an more securely
- Less people move
- Exams can be reviewd remotely

-->

Thinking about the inherent advantages of e-exams, the logistical implications of exams pop into mind. To illustrate this we use the examination process at the KIT as an example <cite>. Although some steps may differ from university to university, the gist remains.

<!-- Hier muss noch mal eine genaue Befragung stattfinden -->

Exams must be printed and stapled. As, exam taking students are numerous, it is common for exams to take place at many different sites. Therefore, on the test day exams must be carried out to the test site. Here, the Ciw of the KIT <KlausDurch> recommends at least two supervisors per test site. On test site, exams must be distributed to students. After the exam is written, exams are collected and counted. They are then carried back to a central location, where they remain until correction. For answer checking, correctors come together, again at a central location, where they then are able to correct the exam. After correction a grade for students is published via internet. Succeeding, an exam revision for students is planned and executed. Lastly exams are archived in their paper form.

It is not supprising that handeling large amounts of paper results in logistics overhead. Removing the paper, subsequentially removes much of the logistics overhead. In an e-exam all of the exam data is digital. There is no printing, since exams are directly transferred to the students device. Further stundets answers can automatically be retrieved after the exam is over. Exam answers are digitally available. The correction of answers is no longer bound to a certain site but can be done remotely. Exam results and feedback can be directly issued to the students. Thus, revision can also be realized decentrally. The digital exam data can then be easly archived.

This comparison illustrates the advantage of e-exams with regard to logistics. Not only is there less movement of employees but more importantly there is no movement of physical paper. Further we find advantages in the digital archiving. Data can be stored space efficiantly with no need for large physical archives. Adding, archives are much saver as redundant backups are feasable and cheap.

**Requirements:**

- Finished exams can be collected remotely.
- Exam data is stored at a central instance and can be accessed remotely.
- Exam data can be arcived.

### The hassel of handwriting

<!--
Bad title. This section focuses soley on time improvement, change it?

- Automated checking is possibel
- Handwriting is bad -> what are the consequences? Only time? Unfairness rises?!
- GUI support is possible, why do we need it?

TD:
- put in citation about effects of handwriting on grading

-->

Checking an exam for correctness is one of the most time-consuming process in conducting an exam. Moving away from paper can reduce this time drastically making use of two things: First, some question types, such as multiple choice can be checked automatically. This is an immediate improvement over correcting these questions by hand. Second, as exam answers are available in digital text reading and checking answers is easier. Answers must not be deciphered, correction of exams can be done faster.

<!--
Adding, the digital nature of exams makes it possible to give visual aid to the corrector. Automatically highlighting specific terminology can help correctors to faster check students answers.
 -->

Further, the replacement of handwriting with digital text has implication for the equality of answer checking. As <James 1927> shows students with bad handwriting get categorically worse grades than students with better handwriting. E-exams can help to make the correction process fairer and less time consuming.

**Requirements:**

- Question types that are able to be checked automatically are checked in such a way.

### Statistics on the fly

<!--
Why do we need statistics, what does it improve? <cite>
-->

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

-->

Part of the complexity and time intensiveness of exam creation lays in creating appropriate questions. Although many courses are not unique to one university, sharing of test question is not common. In paperbased exams there are no standards and there is no suitable collaboration platform. In paper based examination there is no real foundation for sharing and reusing exam questions.

E-exams have to make use of an software artefact in oder to leverage their theoretical benefits. Such a artefact allows for an enforcment of a shareable general format. If users create exams in a specific software, implementing a standard is fairly straight foreward. Such a standard already exits under the name of <QTI 2.2>. Having a standard allowes for educators to collaborate to create exams.

Further this collaboration must not be limited by a singel exam with only a few questions. Exams can come from question pools --- a small subset of questions is selected from a way larger superset. The development and maintenance of a large question pool is very time intensive for a single person, that is why collaboration is so important. Projects in open source software show how collaboration of many can function with great success.

Large question pools do not only help in exam creation, as they allow to produce exams automatically, it also prevents students from knowing the exam beforhand. This will be further ellaborated in the section about cheating.

<!--
Often exam questions are treated as secrets as they are used again and again. This secrecy can not relyably be enforced. It is genral procedure that students collaborate to create in depth Gedächnisprotokolle <cite>, which are then uploaded for public access. Having a large question pool, makes it almost impossible for a student to prepare all questions beforehand, creating a more sound depiction of the students skillset.

As the Zurich University has proposed a general Format for e-exams <cite>, these exam questions are now easily shared among colleges and other universities. These questions can then be collected in so named question pools. At a point where a question pool is large enough, exams can be randomly generated using the exams [!already present in the pool!]. Instead of conceptualizing new exam questions, only the question pool must be taken care of.

Some scholars such as <Handke> have concerns about filling such a question pool <cite>. If this had to be done by one examiner, alone this would really be a serious task but in times of wide spread social media sharing questions or entire pools is worth consideration. As a other way of filling question pools, questions could be thought out by students as exam preperation. Filling the question pool may seem like a daunting task, but making utility of crowd thinking and past experiences can dramatically help this endavour.

Here e-exams show their capabilies in network effects. As more examiners and universities use e-exams, more questions are generated for sharing. Being capable to make use of social media like structures would really help everybody to generate high quality exams fast. As many would argue, it is easier to review an already good selection of questions and pick good ones than to rethink them all from scratch. [!At the moment no sturcture exists which makes use of such ideas...!]
-->

### Partial Open Book Exams

<!--
TODO:
- Bullemie lernen

Moving beyond time and efficiancy improvements.
- Fair depiction of skill
- introduction into open book exams
-->

Untill now I discussed advantages of e-exams that require no rethinking of exam content. E-exams enable assessments to more closely depict a students actual skill level. As the <ETH> states in their paper, examinations should support the purpose of university to produce highly capable individuales. As much of a students academic success is based on their performance in exams, students are highly incentivised to focus their studies on the given exam format. This interdependency between knowledge aquisition and examination shows the importancy of exam design and poses the question of what and how to test.

Questions can be categorized into main groups <ETH>:

- **(Semi) Closed questions**, which mainly revolve around the demonstration of factual knowledge. Solutios are given by using a format like multipe choice [closed] or simple text input [semi-closed](e.g. "What does _BYOD_ stand for?")
- **Competence questions**, which are suited to test for a certain practical skill. Solutions are given in form of an implementation of the specific task at hand. (e.g. "Using the software, implement an e-exam about e-learning.")
- **Essay-type questions**, which are suited for assessing transfer knowledge and understanding. Solutions are given by free text input. (e.g. "Give reasons why subjects in computer engineering are especially well suited for e-exams.")

The last two types can also be set in the context of an open book exam. In which students have access to any resource they feel they need in order to solve the question at hand. These open book tasks most closely reseble real world problems and thus are highly suitable for assessing a students capabilities.

Looking at classical paper based exams we find that they often focus either on (semi) closed questions or on open book questions. As students have access to all relevant facts during the entirety open book exams, testing for fact knowledge in these cases is rendered meaningless.

Still fact knowledge cannot be neglected. For example, consider a doctor, who needs his cheat sheet, in order to conduct open heart surgery. Or an accountant who has to look up the meaning of working capital, every time it shows up. Fact knowledge in the above cases is neccesary, because it is needed immediately. A doctor who does not know his facts may loose lives, an accountant who does not know his vokaulary is nearly useless in any kind of nagotiation. The constraining factor in both cases being time. These examples show that in order to assess for capabilitie a marriage of (semi) closed quesions and open questions is neccessary.

With E-exams it is fairly easy to implement _partial_ open book exams that allow for both open and closed task formats. E-exams can achive this by enacting per question time constraints. Closed questions are imposed with a short answer frame that leaves no time for looking up the actual answer. Further, access to question must be restricted after the time frame has expired.

<!--
These partial open book exams can be realized through time constraints. E-exams can thus provide an environment that resembles real world problems more closely.

Open Book exams depict skills in _high order cognitive processes_ <Krathwohl> way better as they resemble real world scenarios more closely.

Additionally through per question time contostraints closed tasks formats that mainly test for fact knowledge can be implemented. Resulting in partial open book exams.

As e-exams allow easy and equal access to numerous additional resources (i.e. via internet) they make open book exams more feasable.

Seeing exams as an incentive to prepare for reallife problems, it is only sensable to pose questions that resemble reallife problems. Real life problems do not ask for facts but for application and connection of knowledge.

In an exam implementation questions that test for fact knowledge can be seen as closed or semiclosed task formats <ETH>, tasks that rely more strongly on.

Thinking about skillsets reveals another problem of paper based exams. As many have stated, exams often fail to depict real life problems <cite>.

In contrast to exams, real life almost never asks soley for facts, it asks for a brought application of knowledge. It asks for problem solutions, no matter the resource . There is a case to be made to test for fragestellungen <cite>, that come up in real life in order to fairly get a students skill level. When trying to achive this, open book exams may come closest to depicting a real life problem situation <cite>. On the other hand some fact knowledge is of utmost importance <cite>.

[!E-exams on the other hand can provide a mixture of both <cite>.  Consider an exam where in principle every resource could be used. In such an open book exam especially transfer knowledge can easily be tested. As we discussed fact knowledge is also essential part of the examination process. As this fact knowledge, in a real world application must be available in seconds it is only a reasonable thing to just enforce a time restriction to any fact questions.

In this way e-exams can achive a hybrid testing form. It allowes examiners to more reallistically assess a students real capabilities. Moving educational assessments  closer to real world requirements. This also helps to steuer against the trend of Bullemie lernen <cite>. As studendts find themselves forced to wiedergeben sometimes hundereds of pages of scripts, this short term memory is reinforced.

> > E-exams must allow for partial open book exams.

- [ ] Question types!
 -->

### Cheating and randomization

<!--
Impications of cheating:

- !what kinds of cheating is there?
- cheating cannot completely be prevented
- using open book design may weaken cheating
-->

When thinking about any assessment the consideration and handeling of academic dishonesty (e.g. cheating in an exam) is one of the most important parts. Moving from paper to e-exams poses the questions what parts -- if any -- must be adjusted to accomodate for changed circumstances and environments.

In his paper <McGabe> poses seven fields of possible cheating in exams which he then evaluates by accurance and percived severeness. Six of which are relevant for this thesisis purpose. The fields are can be described as follows:

**Student cooperation**:

- **Knowing the questions** Learning what is on an exam from someone who has already taken it.
- **Cooperation with outsiders** Helping someone else cheat on an exam.
- **Cooperation with fellow examinees** Copying from another student on an exam with their knowledge.

**Use of disallowed aid**:

- **Exploit environmental circumstances** Copying from another student on an exam without their knowledge.
- **Use of unauthorised crib/cheat notes** Bringing prepared cheat notes to use in the exam.
- **Use of electronic, unauthorized aid** Using e.g. a smartphone to google or review lecture material.

Before thinking about how to obviate these cheating scenarios an important statement must be made: Cheating cannot completely be eliminated. There are always ways for students to engage in cheating. E-exams cannot change that. But compared to paper based exams some measures against cheating may be more effective.

**Knowing a question.** As the question finding process in a time consuming process, a strategy can be to keep questions as secret as possible and reuse them throughout many exams. This is a rather uneffective strategie as platforms such as studydrive often provide comprehensive protocols from memory of the given exam. E-exams can choose a different approach. Instead of having few questions and keeping them secret, e-exams can levarage collaborative question pools. At a certain point it becomes unfeasable for students to prepare for every available question as question pools grow larger.

**Cooperation with outsiders** and **fellow examinees**. For closed questions this cooperation can be prevented by using strict time restictions. As already stated above these questions fall in the category _Either you know the answer or you don't_ there is no need for a lengthy reflection period. As time constraints are tight, there really is no way of communicating with others and solving the question. For more open question types the time limitation is not as tight. At the same time answers require more in depth considerations. To ensure that students write down their own ideas and cannot share their thoughs, the copy and paste functionallity can be disabled. Further, e-exams can easily be randomized, thus preventing students form peeking or signaling solutions to eachother.

**Exploit environmental circumstances.** Again randomization can solve this problem. As questions appear in a different order for each student even multiple choice questions can not simply be copyed.

**Use of unauthorized cheat notes or electronic aid.** Following the argument made about partial open book exams we find that besides time constraints no additional measures must be enforced. Cheat notes really are not of much help if there is no time to use them.

We find these cheating scenarios to be to a large degree managed by e-exams. Still, as specific software is in use the degree of cheating must constantly assessed and measure against bugs or security flaws must be identified.

<!--
As <cite> found in his paper there are two main categories when it comes to cheating. Planned and spontaineous cheating. Spontainous cheating accures in stress situations where the student feels overwehlmed. It may include looking at other students worksheets or [!even going to the toilet!] to look something up on the internet. Planned cheating on the other hand is intended by the stundet beforhand. The student deposits a cheat sheet in the bathroom, or directly to the exam. Even if the Folgen of cheating are in most cases a failure of the exam, cheating is still common among students. A study of ... found that measures against cheating had almost no effect <cite>.

We must keep this in mind when thinking about e-exams. Against spontaious cheating, some measure can easily be enforced. As tests can be highly randomized looking at a neighbours screen may lead to no new information.

Otherwise, as in a this first step we just replaced paper with a computer there are basically the same eforcements possible. Software such as the open source safe exam browser of the ETH Zürich (link) can be used to make other programs on the device inaccessible during the exam <cite>. So in theory e-exams can be just as safe as paper based exams. In his paper <cite> found that many cheating methods in e-exams can be circumvised by simple measures.

As I discussed earlyer cheating may not even be a big concern if exams rely on (partial) open book. Open book exams do not need restriction of resources. For an open book exam not even software has to be restricted on students devices. This has also the benefit, that such a system has less parts that must be maintained, thus being less prone to errors.

-->

### From central to decentral e-exams

In the previous section I talked about advantages of central e-exams compared to paper based exam. One key characteristic of e-exams is that they are issued via the internet. We can use this to remove any local component of e-exams, thus making them decentalized. In the following, I will talk about advantages that decentral e-exams bare and the implications of decentralizing exams on cheating and infrastructural considerations.

### E-Exams as an logistics problem

<!-- find source to proove its a problem -->

As seen above, e-exams can be immensely more efficient in terms of logistics, compared to a paper based exam. There are however still some shortcomings. First, consider the allocation of students to their respective test taking location. As different students take part in different exams this allocation grows ever more complex and requires lots of planning of a central authority. <!-- Look at software for proof --> Making e-exams decentral allows for this process to be streamlined enourmously.

Second, for supervision of exams human resources are needed. The <KIT> for example recommends two supervisors per location. E-exams can free up some of these resources. To do this we need to take earlier considerations about partial open book exams into account. As I layed out, Partial open book exams allow for tests that do not ask for supervision, making existing supervison obsolete.

When talking about decentralizing e-exams I think it is important to say that the goal is not to force students to write their exams at home. There still can be space reserved for exams by the university. The managemant and supervision of these spaces just becomes magnitudes more easy.

### Cheating

The main points that were made about cheating in section <XX>, still hold true when talking about decentralized exams. A big difference however can be found in the authentication of students. In a central exam each students identity is checkt by an examinee. The students signature and the student identification card provide identification. In decentalized exams this direct checking is no longer possible. There is no satifactory solution to remotly checking a students identity. Still, e-exams have ways to deterr this kind of dishonesty.

A first measure might be to make use of integrated webcams and microphones of the devices at hand. This low key supervison creates a barrier. Students get a feeling of doing really commiting academic fraud. This is important, as students who really put energy into faking their identity can fool the decentral system just as easily as the central system. The sole existance of any measures makes the students behave more honest. Just as video survailance makes crime less common at public places <cite>. This video and sound data can be reviewed if needed.

<!--
We already discussed the need for local storage above. Earlier we takeld about it as a measure against data loss in event of a connection error. Moving e-exams into the decentralized realm poses the need for encrypted storage of data. As data is send from the local storage tempering with the data must be prevented at all cost.
-->

### Infrastructure

I talked about decentralized exams in form of BYOD exams. These devices are heterogenious. They run different operating systems, are produced by different companies and have different specifications. It makes little sense to develop propriatary software for each device. E-exam can although make use of browser technology. As modern web-applications do not lack speed or functionallity and can be adopted cross platform. The software is hosted at a central instance where it can be maintained and improved.

Of course e-exams need a internet connection. Still, connection issues are not a big issue. Through advances in web technologies it is feasable to make web applications available in offline use. Even if the device looses power, exams can be resumed after a reboot.

## Software

In the previous section I laid out areas in which e-exams can improve upon the examination pocess. As I already discussed the actual accurance of these advantages havily depends upon the software that is used in order to implement an e-exam. In the following I will take a look at common solutions:

- Ilias <cite>
- Moodle <cite>
- Blackboard <cite>
- LPlus <cite>
- OpenOlat <cite>

I will measure their quality based on their degree of fullfillment of requirements I layed out earlier.

Befor comparing these solutions there are some features that are met by every tool. Among these are:

- A way to im-/export question and to manage question pools.
- A way to implement all common question types.
- A way to automatically grade closed questions.
- A way to randomize the order of exam questions.
- A in depth documentation and/or community.

### Learn Management System vs. Standalone Solution

Of the five e-exam products four are integrated into full LMS. LPlus being the exception. The degree of usability and richness, highly varies between the tools. Problematically the integration into a LMS makes them unfeasable to exchange. As LMS provide a wide range of features and applications the lock in effect a university experiences is way to large as it could justify changing to another LMS, just to improve testing capabilities. With this consideration in mind stand alone solutions have an advantage. Instead of trying to solve a whole range of e-learnig problems, a dedicated e-examination software focuses to solve a single problem. I will still compare the e-examination capabilities of big LMS as they often are the sole point of contact to e-examination of a university.

### Open Source

In the context of education, large amounts of personal data are generated. Data protection and security play a big role in such an environment. Open source solutions are less prone to major security issues as the development can leverage the crowdsourcing capabilities. Also all processes are transperent there is no worring about the collected data being abused.

Additionally, open source soulutions give universities the abilitiy to host the examination software themselves. In this way confidential student data is always under the direct supervision of the universities.

Of the considerd solutions three of them are fully open source. Blackboard only has a partially open source codebase and LPlus is a closed source software.

### Timing

As I introduced the concept of partial open book exams I showed how important per question time restrictions are. Although all tools allow for time restrictions effecting the whole exam, time constraints enforceable in LPlus and OpenOlat

### Connection issues

One of the biggest shortcomings of the softwares at hand is their way of handeling connection errors. All of them rely on a stable internet connection. Especially with questions that rely on time restrictions, this is problematic. Student answers can be sent to the examination authority after the time limt has expired due to delay in connectivity although a student has answered the question in time.

### Test layout

<!-- When designing a partial open book exam it is important to restrain a students navigational abilities during an exam. If studentns could jump
students cant jup
 --> 

As described above exams must be customizabel in such a way, that students cannot jump between questions and cannot reanswer questions. Also they must only see one question at a the time. This customization is found in Moodle, LPlus and OpenOlat. Both Ilias and Blackboard are very limited in that regard.

<!--
## Problems


This section cannot be called problems! Maybe Worries?

- What problems are there why are they wrong.
- change management/being afraid of new tools

As I have show above e-exams bare many theoratical advantages over paper based exams. In reality these advantages can only be realized through fitting software.

Many <cite> have pointed at problems that may arise from switchig from paper based exams to e-exams. Some of these problems are not of any concern as techincal advancements have made them obsolete.

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
