{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "20201214.ipynb",
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyOsy/d/FLQDsr1CWgNMf1Is",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gusanans218/Python/blob/master/20201214.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sasnM3w2dJ3N"
      },
      "source": [
        "print('신씨가 소리질렀다 \"도둑이야\"')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "od_0vzy3eKC-"
      },
      "source": [
        "a,b = input().split()\r\n",
        "print(int(a)+int(b))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CwJAx_21fYVy"
      },
      "source": [
        "print(\"당신이 태어난 연도를 입력하세요\")\r\n",
        "birth_year = input();\r\n",
        "age = 2020 - int(birth_year)+1\r\n",
        "\r\n",
        "if age <= 26 and age >= 20:\r\n",
        "    print(\"대학생\")\r\n",
        "elif age < 20 and age >= 17:\r\n",
        "    print(\"고등학생\")\r\n",
        "elif age < 17 and age >= 14:\r\n",
        "    print(\"중학생\")\r\n",
        "elif age < 14 and age >= 8:\r\n",
        "    print(\"초등학생\")\r\n",
        "else:\r\n",
        "    print(\"학생이 아닙니다\")\r\n",
        "\r\n",
        "#학생인지 맞추기"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XB_rvCnth3UC"
      },
      "source": [
        "for i in range(1,10):\r\n",
        "    for j in range(2,6):\r\n",
        "        print(str(j)+\"x\"+str(i)+\"=\"+str(i*j)+\" \",end='\\t')\r\n",
        "        print()\r\n",
        "print()\r\n",
        "for i in range(1,10):\r\n",
        "    for j in range(6,10):\r\n",
        "        print(\"%3d x %3d = %3d\" %(i,j,i*j), end='\\t')\r\n",
        "    print()\r\n",
        "\r\n",
        "#구구단"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r38buq0PivA5"
      },
      "source": [
        "print(\"8진수\")\r\n",
        "decimal = int(input())\r\n",
        "result =''\r\n",
        "while (decimal > 0):\r\n",
        "    remainder = decimal % 8\r\n",
        "    decimal = decimal // 8\r\n",
        "    result = str(remainder)+result\r\n",
        "print(result)\r\n",
        "\r\n",
        "#10진수 -> 8진수"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aZoiNqBfjOb1"
      },
      "source": [
        "print(\"16진수\")\r\n",
        "decimal = int(input())\r\n",
        "result1 = ''\r\n",
        "list = ['A','B','C','D','E','F']\r\n",
        "\r\n",
        "while(decimal>0):\r\n",
        "    remainder = decimal % 16\r\n",
        "    decimal = decimal//16\r\n",
        "    if remainder <= 9:\r\n",
        "        result1 = str(remainder)+result1\r\n",
        "    else:\r\n",
        "         result1 = list[remainder -10]+result1\r\n",
        "\r\n",
        "    print(result1)\r\n",
        "\r\n",
        "#10진수 -> 16진수"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qSv5IkhmkIA9"
      },
      "source": [
        "kor_score = [49,80,20,100,80]\r\n",
        "math_score = [43,60,85,30,90]\r\n",
        "eng_score = [49,82,48,50,100]\r\n",
        "\r\n",
        "midterm_score =[kor_score,math_score,eng_score]\r\n",
        "\r\n",
        "for subject in midterm_score:\r\n",
        "    max = 0;\r\n",
        "    sum = 0;\r\n",
        "    for i in subject:\r\n",
        "        if max < i:\r\n",
        "            max = i;\r\n",
        "\r\n",
        "            sum +=i;\r\n",
        "        print(max, sum)\r\n",
        "        print()\r\n",
        "\r\n",
        "\r\n",
        "#과목별 합계, 최댓값"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t_Q2LeUP3KT7"
      },
      "source": [
        "amount, currency = input(\"입력: \").split()\r\n",
        "if currency == \"달러: \":\r\n",
        "    ratio = 1167\r\n",
        "elif currency == \"엔\":\r\n",
        "    ratio = 1.096\r\n",
        "elif currency == \"유로\":\r\n",
        "    ratio = 1268\r\n",
        "else:\r\n",
        "    ratio = 171\r\n",
        "print(ratio * int(amount),\"원\")\r\n",
        "\r\n",
        "#원화변환"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y_1hpZwL4DVU"
      },
      "source": [
        "num1 = int(input(\"num1 :\"))\r\n",
        "num2 = int(input(\"num2 :\"))\r\n",
        "num3 = int(input(\"num3 :\"))\r\n",
        "\r\n",
        "if num1>num2:\r\n",
        "    max_num = num1\r\n",
        "else:\r\n",
        "    max_num = num2\r\n",
        "if num3> max_num:\r\n",
        "    max_num = num3\r\n",
        "print(max_num)\r\n",
        "\r\n",
        "#최댓값 구하기"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nQFafLfh5T5r"
      },
      "source": [
        "#우편번호\r\n",
        "\r\n",
        "zipcode = input(\"우편번호\")\r\n",
        "\r\n",
        "if zipcode[2] in '012':\r\n",
        "    print(\"강북구\")\r\n",
        "elif zipcode[2] in '345':\r\n",
        "    print(\"도봉구\")\r\n",
        "else:\r\n",
        "    print(\"노원구\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xFhyyRuY5opK"
      },
      "source": [
        "#글자 거꾸로 출력\r\n",
        "menu = [\"면라\", \"밥김\", \"김튀\"]\r\n",
        "for food in menu:\r\n",
        "    print(food[::-1])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "me4j3dIi54gU"
      },
      "source": [
        "#대문자만 출력\r\n",
        "list = [\"A\",\"b\", \"c\",\"D\"]\r\n",
        "for word in list:\r\n",
        "    if word.isupper():\r\n",
        "        print(word)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kzkhyzqP6HhY"
      },
      "source": [
        "#파일이름만 출력\r\n",
        "list = ['hello.py','ch02.py','intro.hwp']\r\n",
        "for file in list:\r\n",
        "    tmp = file.split('.')\r\n",
        "    print(tmp[0])\r\n",
        "\r\n",
        "list = ['intra.h','define.c','run.py']\r\n",
        "for file in list:\r\n",
        "    if file.endswith(\"h\"):\r\n",
        "        print(file)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hvoLh26d8Bsl"
      },
      "source": [
        "list=[3,4,4,5,6,6]\r\n",
        "result = []\r\n",
        "for val in list:\r\n",
        "    if val not in result:\r\n",
        "        result.append(val)\r\n",
        "#중복제거"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EJSbDcbu9gZE"
      },
      "source": [
        "num_str=\"720\"\r\n",
        "num_int = int(num_str)\r\n",
        "print(num_int+1, type(num_int))"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
