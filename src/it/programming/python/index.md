# Python

## CLI - Shell

- prompt-toolkit: allows to get a shell in which the user can execute commands.
  - keeps a history of the commands
  - proposal of completion from existing commands and from the history
  - syntax highlighting
  - dialog box (Ex: Important decision)
- PyInquirer: create simple interactions with the user (questions/answers)

### Click

How to use a tag (eg:`@common_options`) for commands that have same options.

```python
def common_options(f: Callable):
	options = [
		click.option(...),
	]
	return functools.reduce(lambda x,opt: opt(x)options,f)
```

## Data visualization

- Pandas, Numpy
- [Matplotlib](../../tools/matplotlib/index.md), Graphviz, Dash, Orange

Recursive unzip with password
```python
import os

number = 556

while number > 0:
	os.system("zip2john zip_"+str(number)+".zip > hash")
	os.system("john --wordlist=rockyou.txt hash > dustbin")
	os.system("john --show hash > needyou")
	f = open('needyou','r')
	lines = f.readlines()
	password = lines[0].split(':')[1]
	f.close()
	os.system("unzip -P "+password+" zip_"+str(number)+".zip")
	os.system("rm zip_"+str(number)+".zip")
	number-=1
```

## Testing in Python

### @pytest.fixture

Run code before a test method

```python
@pytest.fixture
def before_test():
	pass

def test_f1(before_test):
	pass
```

### @pytest.mark

Run test by markers: `pytest.mark.<name>`

```bash
pytest -m <marker>
```

### pytest.mark.parametrize

Run a test again multiple sets of argument

```python
@pytest.mark.parametrize("i,j,o",[(5,5,10),(3,5,12)])
def test_add(i,j,o):
	assert i+j == o,"failed"
```

### @pytest.raises

We expect to have an error.
@pytest.raises(ValueError)

### Command line options


```bash
-s # display prints
-pytest-randomly # run tests in a random order
-pytest-cov # compute code coverage at the same time
```