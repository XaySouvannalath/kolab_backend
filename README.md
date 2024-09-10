# How to run the project:
uvicorn main:app --reload

# How to run the project in real server
 -> myenv/bin/fastapi run main.py

 ->uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4



#get all installed packages list
-> python3 -m  pipreqs.pipreqs . --force

# HOw to install package from requirements.txt file
->myenv/bin/pip install -r reqiurements.txt


# resume session
-> tmux attach -t mysession



# run in server using PM2
pm2 start "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" --name hello_world
pm2 start "myenv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --workers 3" --name kolab_backend -i 3

view-source:https://www.facebook.com/MrBeast6000


task:

get follower log by: influencer_id, from_date to_date


- connect api to real system
- post detail, likes, engagement, reach, video views
- facebook










# set up server
1. mysql
2. nginx
3. firewall 













 224  apt install python3-mysql
  225  pip install =r requirement.txt 
  226  uvicorn main:app --reload
  227  pip install mysql
  228  python -m venv myenv
  229  python3 -m venv myenv
  230  clear
  231  myenv/bin/pip install mysql
  232  myenv/bin/pip install -r requirements.txt 
  233  uvicorn main:app --reload
  234  myenv/bin/pip install mysql
  235  myenv/bin/pip install mysqlclient
  236  sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
  237  myenv/bin/pip install mysqlclient
  238  myenv/bin/pip install mysql
  239  uvicorn main:app --reload
  240  clear
  241  apt install python3-mysql
  242  fastapi run main.py
  243  myenv/bin/pip install fastapi
  244  myenv/bin/python3 main.py
  245  fastapi run main.py
  246  myenv/bin/fastapi run main.py
  247  cd /var/server