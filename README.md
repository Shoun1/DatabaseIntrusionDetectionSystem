## Problem Statement

Modern enterprises face increasing threats to their databases from both external attackers and insider misuse.

Traditional intrusion detection systems (IDS) often struggle to differentiate between harmless probing attempts (dummy/fake attacks) and genuine malicious queries that aim to exfiltrate sensitive data. This leads to either:

i)False positives where legitimate or test activities trigger unneccesary alerts

ii)False negatives, where actual attacks bypass detection

There is a pressing need for a database intrusion detection system (DB-IDS) that can simulate multiple attack scenarios, analyze query behavior, and accurately distinguish genuine attacks from dummy attempts. Such a system should also provide automated responses (blocking, quarantining, alerting) to minimize damage and reduce the burden on security teams.

User stories:
1.As a security analyst I am looking to reduce the false positives of attacks
2.As a developer analyst I am looking to detect the genuine attacks that are seemingly false i.e. 1 means false and 0 means true.
3.As a student I am looking to develop a prototype first for the above two.
