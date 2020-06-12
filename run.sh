cd /workspace/DeepModels

python test.py -e 5 -b 32 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 2 -b 128 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 2 -b 256 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 5 -b 256 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 5 -b 512 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 1 -b 256 -l 0.001
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 10 -b 128 -l 0.1
rm -f cifar10-ckpt-*
sleep 300
python test.py -e 2 -b 128 -l 0.001
rm -f cifar10-ckpt-*

