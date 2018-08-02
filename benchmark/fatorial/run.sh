for i in {1..100000}; do
    curl http://10.11.4.:5000/fatorial/20000 &
done
