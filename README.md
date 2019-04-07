# DTF

Duplicate Thumbnail File - A mathod to indetify duplicate articles when doing a [Systematic review](https://en.wikipedia.org/wiki/Systematic_review).

## The problem

A systematic review could spawn countless articles, when running your search string on different data bases.
Many times articles were exported as PDF files and submited to diferent jornals or publications. The problem is, depending on how the PDF was exported, it will produce a different file, making it hard to check for duplicates by looking at their hash.

## The experiment

Five articles were written and exported to PDF, each one with a small difference.

* **01-jpg-100.pdf** - was exported as a JPG compression with 100% quality.

* **02-lossless.pdf** - was exported as a LOSSLESS compression.

* **03-lossless-2newlines.pdf** - was exported as a LOSSLESS compression with two new lines after the end of the document.

* **04-jpg-80-2newlines.pdf** - was exported as a JPG compression with 80% quality and two new lines after the end of the document.

* **05-jpg-80.pdf** - was exported as a JPG compression with 80% quality.

All documents were created using [Libre Office](https://www.libreoffice.org/).

Let's look at their hash:

| Hash | File |
| -- | -- |
|1db6c720061004b740b87320f0d1d2a68bd9d312 | 01-jpg-100.pdf |
|c9ecd0d02f04637ab81f8f383a74929d8a9f1a40 | 02-lossless.pdf |
|dd8f35b79ded6b61f53eaeb0a9a2a7f1bf34eae6 | 03-lossless-2newlines.pdf |
|9b660130bba4c2c7b63be832aab08a48a2b2e6f5 | 04-jpg-80-2newlines.pdf |
|ffc4a3fcff380929f7c38379f5804e7bbd87ea44 | 05-jpg-80.pdf |

According to the hash of each file, they're different from each other, when in fact, is the "same" document.

## The solution

And what if instead of looking at the hash of each file, we look at their thumbnail? It might work a little better.

So a python script was written to generate the thumbnail of each file and measure how different those thumbnails ware.

Here's the result:

| File 01 | File 02 | Difference |
| -- | -- | -- |
| 03-lossless-2newlines.png | 02-lossless.png | 0.0 |
| 03-lossless-2newlines.png | 05-jpg-80.png | 0.0 |
| 03-lossless-2newlines.png | 01-jpg-100.png | 0.0 |
| 03-lossless-2newlines.png | 04-jpg-80-2newlines.png | 0.0 |
| 02-lossless.png | 05-jpg-80.png | 0.0 |
| 02-lossless.png | 01-jpg-100.png | 0.0 |
| 02-lossless.png | 04-jpg-80-2newlines.png | 0.0 |
| 05-jpg-80.png | 01-jpg-100.png | 0.0 |
| 05-jpg-80.png | 04-jpg-80-2newlines.png | 0.0 |
| 01-jpg-100.png | 04-jpg-80-2newlines.png | 0.0 |

So, as we can see, there is 0.0 difference between them, so they must have the same content.

## Conclusion

This experiment offers a diffent approach to a common problem when doing systemic review, and in this particular case, it worked better. This method could be used alongside with other methods to indentify and exclude duplicate files.

The *dtf.py* script could be used as **base** to a **more robust** script that compares any files that could be visually compared.
