#!/bin/bash

for i in "*.pdf";
	do
		sha1sum $i;
	done
