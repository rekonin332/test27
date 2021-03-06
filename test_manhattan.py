users = {
      "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}
    , "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}
    , "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0}
    , "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0}
    , "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0}
    , "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0}
    , "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0}
    , "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}


def minkowski(rating1, rating2, r):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)

    return pow(distance, 1.0 / r)

# print(minkowski(users['Angelica'], users['Bill'], 2))


def manhattan(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


print(manhattan(users['Angelica'], users['Bill']))

print(manhattan(users['Hailey'], users['Veronica']))


def computeNearestNeighbor(username, users):
    distances = []
    for u in users:
        if u != username:
            # distances.append((manhattan(users[username], users[u]), u))
            distances.append((minkowski(users[username], users[u], 2), u))
    distances.sort()

    return distances

print(computeNearestNeighbor('Hailey', users)[0][1])


def recommend(username, users):
    recommendations = []
    nearest = computeNearestNeighbor(username,users)[0][1]
    neighborRatings = users[nearest]
    userRatings = users[username]

    for i in neighborRatings:
        if i not in userRatings:
            recommendations.append((i, neighborRatings[i]))

    return sorted(recommendations, reverse=True, key= lambda x : x[1])

print recommend('Hailey', users)

print recommend('Angelica', users)

print recommend('Jordyn', users)

# pearson correlation coefficient

from math import sqrt


def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]

            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += x**2
            sum_y2 += y**2

    denominator = sqrt(sum_x2 - sum_x ** 2 / n) * sqrt(sum_y2 - sum_y ** 2 / n)
    if denominator == 0:
        return 0
    return (sum_xy - sum_x * sum_y / n) / denominator


print pearson(users['Angelica'], users['Bill'])
print pearson(users['Angelica'], users['Hailey'])
print pearson(users['Angelica'], users['Jordyn'])

# Cosine Similarity