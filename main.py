{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#word\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "RKbhcrt1yA6i"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "ZY76B9HltZ2k"
      },
      "outputs": [],
      "source": [
        "words = ['play', 'filling', 'bar', 'theatre', 'easygoing', 'date', 'lead', 'that', 'story',  'island']"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x =[w.upper() for w in words]\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8cV9I-f9t4-x",
        "outputId": "92400d28-4ede-4ada-a69b-d37e309f2b6a"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['PLAY', 'FILLING', 'BAR', 'THEATRE', 'EASYGOING', 'DATE', 'LEAD', 'THAT', 'STORY', 'ISLAND']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "newlist =[newlist for newlist in words if len(newlist)>=5]\n",
        "print(newlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8l5r64cqu4__",
        "outputId": "9e1bc950-857c-480d-ef89-eea57fb5b287"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['filling', 'theatre', 'easygoing', 'story', 'island']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "newlist =[newlist for newlist in words if newlist.startswith('t')]\n",
        "print(newlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3nue7elyv2fP",
        "outputId": "846c56f9-6a5a-40ff-d3d4-c3011786b849"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['theatre', 'that']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "#number"
      ],
      "metadata": {
        "id": "LzoHCiLfyKmu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1=[]\n",
        "\n",
        "for x in range(1,10):\n",
        "  c= x**2\n",
        "  list1.append(c)\n",
        "print(list1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b0JE4SL7yNnP",
        "outputId": "51d05741-38dd-4784-f5e4-82905a9fd20c"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "list2=[]\n",
        "\n",
        "for x in range(1,10):\n",
        "  if x%2==1:\n",
        "     c=x**2\n",
        "     list2.append(c)\n",
        "\n",
        "print(list2)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5N1UH9mGyycq",
        "outputId": "ba733405-488c-45db-98e1-f91613657a8f"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 9, 25, 49, 81]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "list3=[]\n",
        "\n",
        "for task3 in range(1,1000):\n",
        "  if task3%8==0:\n",
        "    task33=task3**2\n",
        "    list3.append(task33)\n",
        "print(list3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Diinva1T4J1s",
        "outputId": "5a754687-df73-4cd4-90b2-5b30d5fe6a88"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[64, 256, 576, 1024, 1600, 2304, 3136, 4096, 5184, 6400, 7744, 9216, 10816, 12544, 14400, 16384, 18496, 20736, 23104, 25600, 28224, 30976, 33856, 36864, 40000, 43264, 46656, 50176, 53824, 57600, 61504, 65536, 69696, 73984, 78400, 82944, 87616, 92416, 97344, 102400, 107584, 112896, 118336, 123904, 129600, 135424, 141376, 147456, 153664, 160000, 166464, 173056, 179776, 186624, 193600, 200704, 207936, 215296, 222784, 230400, 238144, 246016, 254016, 262144, 270400, 278784, 287296, 295936, 304704, 313600, 322624, 331776, 341056, 350464, 360000, 369664, 379456, 389376, 399424, 409600, 419904, 430336, 440896, 451584, 462400, 473344, 484416, 495616, 506944, 518400, 529984, 541696, 553536, 565504, 577600, 589824, 602176, 614656, 627264, 640000, 652864, 665856, 678976, 692224, 705600, 719104, 732736, 746496, 760384, 774400, 788544, 802816, 817216, 831744, 846400, 861184, 876096, 891136, 906304, 921600, 937024, 952576, 968256, 984064]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#people"
      ],
      "metadata": {
        "id": "nWCsZRMs8cVD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "people = [\n",
        "    {\n",
        "        \"name\": \"Juan\",\n",
        "        \"age\": 34,\n",
        "        \"n_kids\": 2\n",
        "    },\n",
        "    {\n",
        "        \"name\": \"Pepe\",\n",
        "        \"age\": 27,\n",
        "        \"n_kids\": 0\n",
        "    },\n",
        "    {\n",
        "        \"name\": \"Sonia\",\n",
        "        \"age\": 41,\n",
        "        \"n_kids\": 1\n",
        "    },\n",
        "    {\n",
        "        \"name\": \"Lucía\",\n",
        "        \"age\": 22,\n",
        "        \"n_kids\": 2\n",
        "    },\n",
        "    {\n",
        "        \"name\": \"Leo\",\n",
        "        \"age\": 55,\n",
        "        \"n_kids\": 5\n",
        "    }\n",
        "]"
      ],
      "metadata": {
        "id": "yeod4boZ8hNC"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(len(people))\n",
        "\n",
        "x=0\n",
        "for c in people:\n",
        "    if c[\"n_kids\"] >= 1:\n",
        "      x += 1\n",
        "print(\"num of people have kids = \", x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q1i5q2lI-5QF",
        "outputId": "367fa8e3-c26c-4232-9b2f-afcda20b449f"
      },
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "num of people have kids =  4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "x=0\n",
        "for c in people:\n",
        "\n",
        "    if c[\"n_kids\"] >= 1:\n",
        "      x=0\n",
        "      x += c[\"n_kids\"]\n",
        "\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zTSu8-n6FTaP",
        "outputId": "eaddabdc-ca72-44ab-f490-559761c58f34"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "updated_people = []\n",
        "for person in people:\n",
        "\n",
        "    if person[\"name\"].endswith(\"a\"):\n",
        "\n",
        "        updated_person = {\n",
        "            \"name\": person[\"name\"],\n",
        "            \"age\": person[\"age\"] + 1,\n",
        "            \"n_kids\": person[\"n_kids\"] + 1\n",
        "        }\n",
        "    else:\n",
        "        updated_person = {\n",
        "            \"name\": person[\"name\"],\n",
        "            \"age\": person[\"age\"] + 1,\n",
        "            \"n_kids\": person[\"n_kids\"]\n",
        "        }\n",
        "\n",
        "    updated_people.append(updated_person)\n",
        "\n",
        "print(updated_people)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FshKdYOJdS-_",
        "outputId": "665a6060-d98d-4cf2-9258-b25e41c0987a"
      },
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[{'name': 'Juan', 'age': 35, 'n_kids': 3}, {'name': 'Pepe', 'age': 28, 'n_kids': 0}, {'name': 'Sonia', 'age': 42, 'n_kids': 3}, {'name': 'Lucía', 'age': 23, 'n_kids': 4}, {'name': 'Leo', 'age': 56, 'n_kids': 6}]\n"
          ]
        }
      ]
    }
  ]
}