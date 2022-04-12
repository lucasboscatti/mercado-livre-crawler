import pytz
import requests
import subprocess
from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor


def send_request():
    requests.post(
        "https://mercado-livre-crawler.herokuapp.com/schedule.json",
        data={"project": "mercado_livre", "spider": "offers"},
    )


if __name__ == "__main__":
    subprocess.run("scrapyd-deploy", shell=True, universal_newlines=True)
    scheduler = TwistedScheduler(timezone=pytz.timezone("America/Sao_Paulo"))
    # cron trigger that schedules job every every miday at 12:00
    scheduler.add_job(send_request, "cron", day_of_week="*", hour="12", minute="0")
    # start the scheduler
    scheduler.start()
    reactor.run()
