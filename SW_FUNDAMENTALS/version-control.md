# Table of Contents
  - [Overview](#overview)
  - [Local VCS](#local-vcs)
  - [Centralized VCS](#centralized-vcs)
  - [Distributed VCS](#distributed-vcs)

#   Version Control Systems - An Overview

##  Overview
Manage changes to files, so that they may be recorded

Everything is saved in a repository. Developers must get working copies to develop on for their local machines.

**Benefits**
*   Collaboration
*   Accountability and visibility
*   Isolation
*   Backup & Restore
*   Work Anywhereå

##  Local VCS
*   Tracks files within a local system
*   Replaces "Save a copy before editing"
*   Not meant for most benefits
*   System only saves delta between two files, instead of two files
    *   Delta is reversed to get requested version

##  Centralized VCS
*   Client-Server model
*   Respository is stored on a central server
*   Working copy is acquired by client
*   Only one person can work on a file
    *   Must checkout to work on it
    *   Checkin applies new copy to repo
        *   Tags new version, unlocks for others to change

##  Distributed VCS
*   Peer-to-Peer Model
*   Repository can be stored on server or client
*   Individuals clone repository to work on their changes
*   Full repository on many systems - cna be used to restore
*   Many can work on files simultaneously
*   When change is made - push the file to main repository
*   VCS detects conflicts between version

#   Git (gud)

Distributed VCS that is trendy and open-source.

Git must be installed on a client, and it's focus is on CLI usage

##  Snapshots
Instead of deltas, git stores data as snapshots.
*   If a file does not change, git uses a reference to a p[revious snapshot

##  Three Stages
### Repository
Each client has a full copy of the repository
*   Stored within .git directory
    *   Stores metadata, commits, and logs