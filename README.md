# Ephemeral Context for Music Recommendation

### GET CODE:

```bash
git clone https://github.com/pavelk2/ephemeral-context-music-recommendation ICML
cd ICML
```

### SEE HOW SIMPLE RECOMMENDER WORKS:

```bash
python simple_system.py
```

OUTPUT:

```bash
[ 50.5  50.5  50.5]
[2 4 6]
[ 9.  9.  9.]
[ 10.  10.  10.]
[ 100.  100.  100.]
[2 4 6]
```

### SEE HOW COMPLEX RECOMMENDER WORKS:

```bash
python complex_system.py
```

OUTPUT:

```bash
=========
('context: ', [1, 2, 3, 4, 5, 6, 7, 8])
('Individual recommendations: ', array([  1.,   1.,  20.]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 9.7,  6.7,  5.6]))

=========
('context: ', [0, 0, 0, 0, 0, 0, 0, 0])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [9, 9, 3, 4, 5, 6, 7, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [1, 2, 3, 10, 5, 6, 7, 8])
('Individual recommendations: ', array([  1.,   1.,  20.]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 9.7,  6.7,  5.6]))

=========
('context: ', [10, 2, 30, 4, 50, 6, 70, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))

=========
('context: ', [100, 200, 30, 100, 50, 6, 70, 8])
('Individual recommendations: ', array([10, 20, 30]), array([30, 20, 10]), array([1, 1, 1]))
('Final recommendation: ', array([ 10.6,   8.6,   6.6]))
```
