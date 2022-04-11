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
<<<<<<< HEAD
    # cron trigger that schedules job every every day at 15:00
    scheduler.add_job(send_request, "cron", day_of_week="*", hour=15, minute=0)
=======
    # cron trigger that schedules job every every miday at 12:00
    scheduler.add_job(send_request, "cron", day_of_week="*", minute="*/20")
>>>>>>> 4d0d69c420b9a5f788f2b1d3c36266b3d0b08df4
    # start the scheduler
    scheduler.start()
    reactor.run()
