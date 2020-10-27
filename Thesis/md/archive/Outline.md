# An Outline

## The main research question.

> Which requirements need to be matched to allow for sound competence testing, in form of decentralized e-exams?

## Looking at the problem and why it is of interest

The examination process is often a **tedious task** for those who are in charge. Great amounts of time go into organizational problems. Digitizing exams would resolve many of these problems. A step towards electronic examination would make the process more flexible, scalable and resource-efficient. Meanwhile, leading to a more accurate depiction of a students' competence.

Taking the current pandemic under consideration, it may not be an option to just move from paper to e-exams. Exams thus must be conducted decentralized, i.d. students take their exams at home.

It is important to notice, that _Decentralized E-exams (DE-exams)_ differ from _paper based exams (PB-exams)_ and even from _centralized e-exams (CE-exams)_ in some key points. Foremost, the examiner has less control over the environment the exam is taken under. This raises questions about exam integrity and fairness. These questions must be addressed through careful conceptualization of questions and intelligent [software] design.

## Is it an unsolved problem?

Digitizing exams is no new idea. Although, most concepts and implementations focus on conducting e-exams in the same environment as _PB-exams_. With regard to COVID-19 this is not an option. Of course some _DE-exams_ are **already conducted** today. These exams are, for the most part, making use of a **proctoring system**. In such a system a supervisor can access the examinees' device, can monitor all their activity and will watch them through their webcam. This proctoring process is costly. It hardly scales and still easily can be fooled.
Further, test-taking applications are found in many _LMS' (Learn Management Systems)_ such as Ilias, Moodle or Blackboard. Unfortunately, most often these applications focus on student self-assessment. They also majorly **vary in quality and utility**. As they are integrated in a complete LMS, changing to the _best_ implementation is in many cases not an option.
Last, as exam data is **highly confidential**, there is a strong argument to be made against closed source solutions. It is crucial to know exactly how the used application works and how data is handled. Adding, open source projects are less prone to major security issues as the development can leverage the crowdsourcing capabilities that an open source system provides.

## An overview of criteria and derived questions

The main criteria emerge as:

- The electronic examination process must be advantageous compared to paper based examination.
- The exam has to have a high level of integrity. Students cannot fake their identity, cheat, cooperate, use disallowed aid or access exam questions beforehand.
- The exam questions must aim to fairly extract a students' skill level.
- Students must be treated equally in the answer checking process.
- The e-exam taking process must be at least be as stress-free as the paper base equivalent.

Having identified these main criteria, I will ask _sub-research questions_ on how to meet these criteria. In doing this I will give insight into how other systems perform.

Version: 2.0.3
