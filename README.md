# AI-ID3/c4.5-algorithm

### Toolbox

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Description
Implementation of ID3/c4.5 tree generating algorithm.

### Status

28.04.2022
- Basic dependencies, start development stage.

02.05.2022
- Basic working version.

### Example of working

All you need to do is just put your JSON data in `inputdata` in `input.json` file.

There is only **one** condition for the correct operation of the algorithm.

- Decision parameter needs to be placed on last place of every input record in `JSON`.

As a result you will get the tree, that is going to look like this, where number on the right side tell about quantity of records dedicated to this rule:

```
Lzawienie
 -- zmniejszone -- 12
|
 -- normalne
|
	Astygmatyzm
	 -- nie -- 5
	|
	 -- tak
	|
		Wiek
		 -- mlody -- 2
		|
		 -- prestarczy -- 1
		|
		 -- starczy
		|
			Wada_wzroku
			 -- krotkowidz -- 1
			|
			 -- dalekowidz -- 1
```

---
