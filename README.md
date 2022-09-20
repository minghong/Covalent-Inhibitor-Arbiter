# Covalent-Inhibitor-Arbiter


## Version: 1.0

Covalent-Inhibitor-Arbiter是一个判断某个化合物是否具有共价特征的判别器。它采用随机森林模型，数据集是来自CovalentInDB的4445个共价药物和来自drug central的4052个非共价药物，通过Mordred获得这些药物分子的1407个分子描述符来进行训练，模型的正确率可以达到93%以上。为了进一步提高判别共价化合物正确率，我们采用多次判断的方式（即只要有一次被判断为非共价化合物，就将它判断为非共价化合物），这样会使结果不会出现假阳性。

## Installation
### Requirements

* 64 bit Linux OS
* Anaconda3: RDkit、mordred

### Downloading and tar
You can download LJA source code [here](). 
