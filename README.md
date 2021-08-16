# Website Checker

Website Checker is a simple program that checks if the inputted website is alive or dead.

If any sites were dead, then it will forward a message to the appropriate channel in Slack.

## Installation

Clone it via [git clone](https://github.com/git-guides/git-clone) to install Website Checker and run.

```bash
git clone https://github.com/boonjo/WebsiteChecker.git
```

## [Ofelia](https://github.com/mcuadros/ofelia)

Ofelia is a modern and low footprint job scheduler for docker environments.

This is implemented to schdeule and automate the process of checking websites.
From docker-compose.yml, you can see:

```yml
labels:
      ofelia.enabled: "true"
      ofelia.job-exec.app.schedule: "@every 1m"
      ofelia.job-exec.app.command: "websiteChecker"
```

it is enabled by the first label, then it can be scheduled with the time interval preference of the user, and lastly choose which command to run. 

From the example above, it will run websiteChecker every minute. 
