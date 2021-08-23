import psutil

for process in psutil.process_iter():
    try:
        if process.name() == "LeagueClientUxRender.exe":
            process.kill()
    except:
        pass