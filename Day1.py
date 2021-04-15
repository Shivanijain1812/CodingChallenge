{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Twinkle, twinkle little star,\n",
      "\tHow I wonder what you are! \n",
      "\t\tUp above the world so high,\n",
      "\t\tLike a daimond in the sky.\n",
      "Twinkle, twinkle, little star,\n",
      "\t\tHow I wonder what you are!\n"
     ]
    }
   ],
   "source": [
    "#Print the poem\n",
    "print(\"Twinkle, twinkle little star,\\n\\tHow I wonder what you are! \\n\\t\\tUp above the world so high,\\n\\t\\tLike a daimond in the sky.\\nTwinkle, twinkle, little star,\\n\\t\\tHow I wonder what you are!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PYTHON VERSION:\n",
      "3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]\n",
      "VERSION INFO:\n",
      "sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)\n"
     ]
    }
   ],
   "source": [
    "#Print sys version\n",
    "import sys\n",
    "print(\"PYTHON VERSION:\")\n",
    "print(sys.version)\n",
    "print(\"VERSION INFO:\")\n",
    "print (sys.version_info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Date & Time :  04-15-21 00:45:59\n"
     ]
    }
   ],
   "source": [
    "#Print current date and time\n",
    "import datetime\n",
    "now = datetime.datetime.now()\n",
    "print(\"Current Date & Time : \",now.strftime(\"%m-%d-%y %H:%M:%S\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the radius of the circle : 1.1\n",
      "The area of the circle with radius 1.1 is: 3.8013271108436504\n"
     ]
    }
   ],
   "source": [
    "#Area of circle\n",
    "from math import pi\n",
    "r = float(input (\"Input the radius of the circle : \"))\n",
    "print (\"The Area of the circle with radius \" + str(r) + \" is: \" + str(pi * r**2))\n",
    "#whenever you concatinate a number with a string it is a good practise to convert that number into string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your first name:Shivani \n",
      "Enter your last name:Jain\n",
      "Your name in reverse : Jain Shivani \n"
     ]
    }
   ],
   "source": [
    "#Accept the user's first and last name and print them in reverse order with a space between them.\n",
    "Fname = input(\"Enter your first name:\")\n",
    "Lname = input(\"Enter your last name:\")\n",
    "print(\"Your name in reverse : \" + str(Lname) + \" \" + str(Fname))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the numbers sperated by commas: 1,3.5,4\n",
      "LIST:  ['1', '3.5', '4']\n",
      "TUPLE:  ('1', '3.5', '4')\n"
     ]
    }
   ],
   "source": [
    "#Accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers\n",
    "num = input(\"Enter the numbers sperated by commas: \")\n",
    "list = num.split(\",\")\n",
    "print(\"LIST: \", list)\n",
    "tuple = tuple(list)\n",
    "print(\"TUPLE: \", tuple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the filename: shivani.py\n",
      "The extension of the file is : 'py'\n"
     ]
    }
   ],
   "source": [
    "#Accept a filename from the user and print the extension of that\n",
    "filename = input(\"Enter the filename: \")\n",
    "file_ext = filename.split(\".\")\n",
    "print(\"The extension of the file is : \" + repr(file_ext[-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Red Black\n"
     ]
    }
   ],
   "source": [
    "#Display the first and last colors from the following list.\n",
    "color_list = [\"Red\",\"Green\",\"White\" ,\"Black\"]\n",
    "print(color_list[0],color_list[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The examination will start from : 11 / 12 / 2014\n"
     ]
    }
   ],
   "source": [
    "#Extract the date\n",
    "exam_st_date = (11,12,2014)\n",
    "print( \"The examination will start from : %i / %i / %i\"%exam_st_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: 5\n",
      "615\n"
     ]
    }
   ],
   "source": [
    "#Accept an integer (n) and computes the value of n+nn+nnn.\n",
    "n = int(input(\"Enter the number: \"))\n",
    "n1 = int (\" %s \" % n)\n",
    "n2 = int (\" %s%s \" % (n,n))\n",
    "n3 = int (\" %s%s \" % (n,n2))\n",
    "print(n1+n2+n3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
