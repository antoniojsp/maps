if [ $1 = env ]
then
  python3 -m venv env
  source env/bin/activate
elif [ $1 = run ]
then
  python3 jinja_test.py $2
fi
