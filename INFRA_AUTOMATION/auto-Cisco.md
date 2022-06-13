# Cisco Automation Solutions
## Read-only automaton
Gather information about the network environment over-time, and determine changes that have been made
Minimize breakage while learning the API, and can audit the configuration

## Activiting Policies and providing Self-Service
You can safely enable users to provision their own updates
Automate onboarding workflows, manage day-to-day, and run through day(n) scenarios

## Deploy Applications, Network Configs, etc. Using CI/CD
Monitor and proactively manage users and devices, gaining insights with telemetry data

# Why do we need automation?
* Speed and agility allow a business to explore oppurtunities before competition
* Scvaling allows a business to scale with demand
## Disadvantages of manual operations
* Time for IT Staff to manually setup environment
* Manual processes are slow and do not easily scale
* Manual processes are subject to human error, automation builds-to-state
## Financial Costs
* Outage costs to a business
* Security risks if breach occurs
## Dependency risks
Software is currently decentralised. No need to manage a full-stack solution.
FOSS provides many collaborative works
Responsible devs try to anticipate and minimise the impact of updates and new releases

**However, new requirements and risks**
* Components need to be fliexible and configurable
    * UNOPINIONATED -> no preference for specific configuration or architecture
* Component developers may abvandon support for old feastures or edge-case integrations
    * May be difficult or impossible to test for all edge-cases
* Dependency-ridden setups tend to get locked into fragile deployment stacks
    * Cannot easily be managed, deployed, improved, or scasled

# Why full-stack automation?
**Benefits can be summarized as*
* Speed
* Repeatability
* Work at scasle with reduced risk

## Self-Service
Self-service frameworks allow users to provision their infra on demand
* Development and testing platforms
* Shared infrastructure components
* Hardened web servers
    * Other appplication instances
* Analytics platforms like Hadoop, Elastic Stack, and Splunk
## Scale On-Demand
Scale to demand
* Cloud bursting
* Traffic-shaping
* autoscale vms or containers on a serverless fgramework
## Observability
Infer the state of a system from it's outputs
* Proactive testing for failure modes and performance issues
* IRL, sauper complex and ephgermeral objects
* We need asutomation to make these short-lived objects observable
## Automated Problem Mitigation
### Chaos Engineering
* Failure is normal
* As application scale, some parts are always failing
* Applications should be engineered to
    * Minimise the "blast radius" of issues
        * route traffic to alternative capavity
        * reduce end-user impact
    * Self-heal
        * allocate resources according to policy
        * redeploy failed componenets as needed to return to healthy
    * Monitor events
        * remember everything that led to incident
        * Determine root-cause
 Some people even advocate using automation tools to cause controlled failures in prod
 * Challenge Dev and Ops to anticipate issues
 * Build in more resilience and self-healing
 * Failure injection testing
**Examples**
* Chaos Monkey
* Gremlin
