---
Author: Jasper Anders
---

# Which requirements need to be matched to allow for sound competence testing, in form of decentralized e-exams?

Tags:

- <cite>: Needs citation
- <!--  --> : Comment
- <review> : need review
- [!!]: Marked, bad sentence or word

## Introduction

## The case for e-exams

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

E-education is a much discussed topic. Much of the educational material has become mostly digital. Still, paper based exams are the way to go, when it comes to assessments in German higher education. Altought some universities amonge these are the FU Berlin and Johannes Gutenberg University Mainz have implemented some way of e-assessment, it still lacks wide application.

In a first step, I will talk about central e-exams. These are coducted under the same circumstances as paper based exams (i.d. students come together in a lecture hall, instead of paper they use a computer to complete the exam). As I want to give intuition, why moving to a _decentralized_ e-examination system might be benificial, I will not discuss other ways of realizing central e-exams then the _bring-your-own-device_ (BYOD) approach. BYOD exams are conducted in the same environment as paper based exams are, the difference being that students bring their tablet or laptop to take the exam on their own device. The BYOD concept is not new. For example Robert Peregoodof talked about the BYOD implementation of the University of British Columbia in the <Glm> conference.

It is important to note that moving from paper based exams to e-exams should be a strict uprgrade. Still, paper based exams and e-exams are different in some key points. Some things that were considerated best practice must be reevaluated and rethought adequately fit the e-exam context. As I will show these changes do not limit the examination process but rather improve it.

When compared to paper based exams e-exams provide many advantages as <Handke> disscuss in their book. I will focus on two different types of advantages that e-exams provide. The fist type are inherent advantages. These are advantages that arise from soly digitizing a paper based exam. We find many of these adavantages in the efficiency of the assessment process.

The other type of advantages are created through additional considerations and by rethinking how paper based exams approach the examination process. These advantages arise mainly from improvements in testing accuracy and equality.

## Exams as a logistics problem

<!--
Is this really the first thing that i talk about?

- Exams can be corrected remotely
- Exams can be archived faster an more securely
- Less people move
- Exams can be reviewd remotely

-->

Thinking about the inherent advantages of e-exams, the logistical implications of exams pop into mind. To illustrate this we use the examination process at the KIT as an example <cite>. Although some things may differ, the gist remains.

<!-- Hier muss noch mal eine genaue Befragung stattfinden -->

Exams must be printed and stapled. As, exam taking students are numerous, it is common for exams to take place at many different sites. Therefore, on the test day exams must be carried out to the test site. Here, the Ciw of the KIT <KlausDurch> recommends at least two supervisors per test site. On test site, exams must be distributed to students. After the exam is written, exams are collected and counted. They are then carried back to a central location, where they remain until correction. For answer checking, correctors come together, again at a central location, where they then are able to correct the exam. After correction a grade for students is published via internet. Succeeding, an exam revision for students is planned and executed. Lastly exams are archived in their paper form.

<!-- this is too long and obivious?! -->

It is not supprising that handeling large amounts of paper results in logistics overhead. Removing the paper, subsequentially removes much of the logistics overhead. In an e-exam all of the exam data is digital. There is no printing, since exams are directly transferred to the students device. Further stundets answers can automatically be retrieved after the exam is over. Exam answers are digitally available. Some, such as multiple choice questions can be automatically evaluated. The correction of the remaining answers is no longer bound to a certain site but can be done remotely. Exam results and feedback could be directly issued to the students. Thus, revision could also be realized decentrally. The digital exam data can then be easly archived.

This comparison illustrates the advantage of e-exams with regard to logistics. Not only is there less movement of employees but more importantly there is no movement of physical paper. Further we find advantages in the digital archiving. Data can be stored space efficiantly with no need for large archives. Adding archives are much saver as redundant backups are a feasable and cheap possibilit.

## The hassel of handwriting

<!--
Bad title. This section focuses soley on time improvement, change it?

- Automated checking is possibel
- Handwriting is bad -> what are the consequences? Only time? Unfairness rises?!
- GUI support is possible, why do we need it?
-->

Checking an exam for correctness is one of the most time-consuming process in conducting an exam. Moving away from paper can reduce this time drastically making use of two things: First, some question types, such as multiple choice, true or false can be automatically checked. This is an immediate improvement over correcting these questions by hand. Second, as exam answers are available in digital text reading and checking answers is easier. Answers must not be deciphered, correction of exams can be done faster.

## Statistics on the fly

<!--
Why do we need statistics, what does it improve? <cite>
-->

Thinking of the digital nature of exam data another advantage emerges. The digital nature of e-exams allow for a fast creation of statistics. Whereas in paper exams every piece of information must be manually digitized, e-exams are digital out of the box. Thus, analasys of exams becomes more feasible. Thinkable are statistics about general performance, but also analasys of specific questions, or student groups. As the exam is the sole indicator of a students understanding of the matter at hand, it is of utmost importance to understand where students struggle and what they are capabil of. Having easy access to exam data yields the possibility of both better exams and better courses.

## Drinks at the pool

<!--
Stupid name.

- Show power of collaboration im question pools. <cite>
- Students can fill your question pool.
- exam question must not be treated as sectets any more
- ? a social network for question sharing??
- refer to open source as model
-->

Part of the complexity and time intensiveness of exam creation lays in creating appropriate questions. Although many courses are not unique to one university, sharing of test question is not common. This might be due to the fact that paper based exams do not provide a foundation for collaboration. In paperbased exams there are no standards. Just as there is no elegant way of sharing exams, there is no way of easily using someones exam questions.

E-exams have to make use of an software artefact in oder to leverage their theoretical benifits. Such a artefact allows for an enforcment of a shareable general format. If users create exams in a specific software, implementing a standard is fairly straight foreward. Such a standard already exits under the name of <QTI 2.2>. Having a standard allowes for educators to collaborate to create exams.

Further exams must not be limited to only a few questions. Exams can come from question pools --- a small subset of questions is selected from a way larger superset. With a large enough question pool exams can be generated automatically. The developmetn and maintenance of a large question pool is very time intensive for a single person, that is why collaboration is so important. Just like open source project are able to  

As the Zurich University has proposed a general Format for e-exams <cite>, these exam questions are now easily shared among colleges and other universities. These questions can then be collected in so named question pools. At a point where a question pool is large enough, exams can be randomly generated using the exams [!already present in the pool!]. Instead of conceptualizing new exam questions, only the question pool must be taken care of.

Some scholars such as <Handke> have concerns about filling such a question pool <cite>. If this had to be done by one examiner, alone this would really be a serious task but in times of wide spread social media sharing questions or entire pools is worth consideration <!-- has this been done?? --> . As a other way of filling question pools, questions could be thought out by students as exam preperation <!-- where does this come from -->. Filling the question pool may seem like a daunting task, but making utility of crowd thinking and past experiences can dramatically help this endavour <!-- this is too sloppy -->.

Here e-exams show their capabilies in network effects. As more examiners and universities use e-exams, more questions are generated for sharing. Being capable to make use of social media like structures would really help everybody to generate high quality exams fast. As many would argue, it is easier to review an already good selection of questions and pick good ones than to rethink them all from scratch. [!At the moment no sturcture exists which makes use of such ideas...!]

Having created a big enough question pool does not only help in exam creation, it also prevents students from knowing the exam beforhand. Often exam questions are treated as secrets as they are used again and again. This secrecy can not relyably be enforced. It is genral procedure that students collaborate to create in depth Gedächnisprotokolle <cite>, which are then uploaded for public access. Having a large question pool, makes it almost impossible for a student to prepare all questions beforehand <!-- just like in a drivers license exam --> , creating a more sound depiction of the students skillset.

## A fair depiction of skill

<!--
Moving beyond time and efficiancy improvements.
- Fair depiction of skill
- introduction into open book exams
-->

Till now I discussed advantages of e-exams that require no rethinking of the examination process in general, we mearly found ways to increase efficency.

Although this is surely one key point in moving from paper based exams to e-exam, e-exam give us the possibility to improve also upon the examinees site of testing. In this section we will take a look at how this may be achived.

As Handke said in his book, we should not look at exams mearly as a service <cite>. Exams should improve the students thinking and ... (Bezug).

Thinking about skillsets reveals another problem of paper based exams. As many have stated, exams often fail to depict real life problems <cite>. In contrast to exams, real life almost never asks soley for fakts, it asks for a brought application of knowledge. It asks for problem solutions, no matter the resource <!-- this is not sharp enought -->. There is a case to be made to test for fragestellungen <cite>, that come up in real life in order to fairly get a students skill level. When trying to achive this, open book exams may come closest to depicting a real life problem situation <cite>. On the other hand some fact knowledge is of utmost importance <cite>.

<!-- is this to free? --> Consider a doctor, who needs his cheat sheet, in order to conduct open heart surgery. Or an accountant who has to look up the meaning of working capital, every time it shows up. To make later reasoning more obvious, it is useful to think about why these two examples are considered a no go. The fact knowledge should be there, because it is needed immediately. A doctor who does not know his facts may loose lives, an accountant who does not know his vokaulary is nearly useless in any kind of nagotiation. The constraining factor in both cases being time. If no real world problem whould have time relevance, it could be argued that fact knowledge is fairly useless. Especially with the internet, where almost any fact knoledge is easier accessible than ever. The truth is, time almost always plays a major role in many problems, so to accrurately depict someones capabilities, there must be some way of checking for fact knowledge. Paper based exams do not allow for a marriage of fact questions and those who ask for transfer whith no restrictions to resources (e.g. the internet, tools and programs).

E-exams on the other hand can provide a mixture of both <cite>. <!-- can it really, there need to be facts here --> Consider an exam where in principle every resource could be used. In such an open book exam especially transfer knowledge can easily be tested. As we discussed fact knowledge is also essential part of the examination process. As this fact knowledge, in a real world application must be available in seconds it is only a reasonable thing to just enforce a time restriction to any fact questions. <!-- there must be checking if this works -->

In this way e-exams can achive a hybrid testing form. It allowes examiners to more reallistically assess a students real capabilities. Moving educational assessments <!-- adapting the skillset better --> closer to real world requirements. This also helps to steuer against the trend of Bullemie lernen <cite>. As studendts find themselves forced to wiedergeben sometimes hundereds of pages of scripts, this short term memory is reinforced.

> > E-exams must allow for partial open book exams.

- [ ] Question types

## Change and scale

<!-- This is not really of interest. -->

Some scolars express concerns about the infrastructural scalability of e-exam systems. In their eyes, exams only provide utility with X students or more being part of the exam. This argument ignores the scaleable nature of the an exam system. Moving to e-exams must not be a decision of one course or one Lehrstuhl alone.

- [ ] Größe von e-exams

## Cheating and randomization

<!--
Impications of cheating:

- !what kinds of cheating is there?
- cheating cannot completely be prevented
- using open book design may weaken cheating
-->

When thinking about any assessment the consideration of academic dishonesty (e.g. cheating in an exam) is one of the most important parts. Moving from paper to e-exams poses the questions what parts -- if any -- must be adjusted to accomodate for changed circumstances and environments.

As <cite> found in his paper there are two main categories when it comes to cheating. Planned and spontaineous cheating. Spontainous cheating accures in stress situations where the student feels overwehlmed. It may include looking at other students worksheets or [!even going to the toilet!] to look something up on the internet. Planned cheating on the other hand is intended by the stundet beforhand. The student deposits a cheat sheet in the bathroom, or directly to the exam. Even if the Folgen of cheating are in most cases a failure of the exam, cheating is still common among students. A study of ... found that measures against cheating had almost no effect <cite>.

We must keep this in mind when thinking about e-exams. Against spontaious cheating, some measure can easily be enforced. As tests can be highly randomized looking at a neighbours screen may lead to no new information.

Otherwise, as in a this first step we just replaced paper with a computer there are basically the same eforcements possible. Software such as the open source safe exam browser of the ETH Zürich (link) can be used to make other programs on the device inaccessible during the exam <cite>. So in theory e-exams can be just as safe as paper based exams. In his paper <cite> found that many cheating methods in e-exams can be circumvised by simple measures.

As I discussed earlyer cheating may not even be a big concern if exams rely on (partial) open book. Open book exams do not need restriction of resources. For an open book exam not even software has to be restricted on students devices. This has also the benefit, that such a system has less parts that must be maintained, thus being less prone to errors. <!-- this is not very good. -->

## Making the move seamless

As briefly touched upon, e-exams must be at least as comfortable as their paper based counterpart. This especially is important when we think about nature of e-exams. As e-exams rely in a client server model they also rely on internet connection.

## Problems

<!--
This section cannot be called problems! Maybe Worries?

- What problems are there why are they wrong.
- change management/being afraid of new tools
-->

Many <cite> have pointed at problems that may arise from switchig from paper based exams to e-exams. Some of these problems are not of any concern as techincal advancements have made them obsolete.

<cite> have talked in their paper about the provision of technical infrastructure. They pose a question about the utility and scale of such a infrastukture. As the [paper] aged the techinical sircumstances changed, nowadays it is almost universal for students to have access to a webbrowser <!-- why a web browser? see section about technical requirements --> . And really thats all they need. Although not recommended, exams could really be taken on any smartphone. <!-- good gist. bad writing. -->

Another concern touches upon connection problems <cite>. There is no doubt upon e-exam using a client--server structure <!-- technical requ. -->. Dependant on the implementation, this may make e-exams prone to connection errors. For example if after every question a new question must be fetched from the server having connection errors can quickly ruin the exam for anyone that is taking it.

> Req: e-exams must sustain in unreliable connection environments

<!-- this has to come in the solution part. --> On the other hand there is the possibility to store the exam and the given answers in the local storage of the browser. As long as the browser is not reinstalled or forced to clear its chache the exam information is secure. To prevent fiddelling with the local chache it could be encrypted. Using this method e-exams could be counducted even be conducted offline, only to send in the exams solution and to download the exam questions an internet connection would be needed. Of course such a soulution must be tested firmly to make sure that any way of hacking the exam is prevented.

With regard to the configuration and usage of an e-exam tool, it is clear that a soulution that is easily usable for novice users but yields potential for more advanced users is of utmost importance. <!-- only problems, not solutions --> Examiners must have the chance to learn the new tool, ideally this is supported by the usage of hight standards of user interface design.

Politics and angst also play into the above problems. As new technologie and software often creates a sense of being overwhelmed there must be a strone emphasis on showing examiners the advantages an e-examination system could give them. E-exams especially show their potential when being widely adopted. As more usage of e-exams can lead to network effects. Especially inside an institution there must be enforcement of the usage of new systems. The faster a new way of working gets adapedt the faster it can improve. In this way also small exams are very valuable. It is even thinkable to get immediate feedback of the examinees to improve the system or to get a students feelings about the exam. As the examination infrastructure is easily scalable, there is not need for smaller exam groups to move back to paper. Questions and questionpools can be created in the same way as for bigger exams and as a new e-exam does not need more resources there is no need to hold back.

=======================================

## From central to decentral e-exams — moving up the ladder

The previous section was about moving away from paper and how this can benefit the examination process. To now improve upon that process even further, we must look at the shortcomings of centralized e-exams.

## E-Exams as an logistics problem

<!-- find source to proove its a problem -->

As seen above, e-exams can be immensely more efficient in terms of logistics, compared to a paper based exam. There are however still some shortcomings. First, consider the allocation of students to their respective test taking location. As exams completely get replaced, as their are not test taking locations any more. This makes the process of exam coordination way easier.

Second, an exam takes many humans to supervise students during their exam. This can be improved by e-exams. To ensure, these improvements really take effect we need to take earlier considerations into account. As we discussed open book exams are realizable quite easily using e-exams. As open book exams allow for the use of any material, for the einschränkung of Material usage there really is no need for supervision.

## Cheating

A nother reason for supervison might be that, students collaborate and thus cheat the idea of open book exams. This can be counterd through the use of heavy randomization. As students encounter questions at different times, collaboration to answer them is hardened. Also copy and pasting must be repressed, as it allows for quick sharing of answers.

We already discussed the need for local storage above. Earlier we takeld about it as a measure against data loss in event of a connection error. Moving e-exams into the decentralized realm poses the need for encrypted storage of data. As data is send from the local storage tempering with the data must be prevented at all cost.

## Less distractions

Some studies find that exams are full of distractions <cite>. They create a stressfull atmosphere. This is especially bad for studentes. Taking exams at home can eliminate this stress factor. Even students who do not have a quite place to write their exams, there could be made room for examiees in either libaries or lecture halls <!-- this is very sloppy --> . Because students dont need any supervision and no special equipment they really are independent from any place.

## Identity

We may delay cheating and cooperation through different measures such as time restictions and randomization. How can we now check if the student we are examing really is the student we want to examine. There is no satifactory answer to this question. In a paper paper based exam student identity is überprüft by the examiner. By looking at the student identity card and letting the student sing the identiy is prooven. If there would really be a big concern about students taking other students exams, checking a students identiy this way is easily fooled. The testtaker must only somewhat resemble the testaker, as the student ids photographs have bad resolutions and are only glanced upon. It can be argued that letting someone take your whole exam is simply to risky.

To get at least some information about the identity of the test taker and to make the hurdle to cheat higher, students could be monitored by their webcams or their smartphones. As alone the thought of being watched already reduces the thought of doing something naughty makes many students rethink their desire to cheat.

As a nother measure, the microphone might also be accessed. Tapping into what the student hears helps examiners to make out if a student is talkig to someone else. Through the use of audio meters and stichproben not every students video feed must be watched, only where verdacht is imment a investigation can be angebracht.

- [ ] cooperation

=======================================

## Bonus

University as a way to help you gain knowledge not a way to test it.

## Moving beyond the limits of education

Education really is a problem of scale. Many studies have shown that the big inequalities that we see today in part are enabled by inequalities in education. Through an open education program many universities aim to dwarf this inequality. The biggest parts of the universities education are: Lectures, tutorials and exams. Today already you can view some of the best lectures online, for free. As Harvard takes part in a open education program. Second, through the rise of plattforms such as the stackexchange stack tutorials have become somewhat crowdsolved. Finding a solution to broughtly test students no matter their location would make a enormous step in the right direction.
