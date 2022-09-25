import numpy as np

def norm_V(p1, p2): # 벡터의 교차곱
    h = np.cross(p1, p2)
    H = h/np.linalg.norm(h)
    return H

#  두 벡터 사이의 회전 각
def roatation_theta(h1, h2):
    return np.arccos(np.dot(h1,h2)/(np.linalg.norm(h1)*np.linalg.norm(h2)))

# 회전 행렬 생성
def rotation_matrix(vec1, vec2):

    H = norm_V(vec1, vec2)

    thetha = roatation_theta(vec1, vec2)

    cos = np.cos(thetha)
    sin = np.sin(thetha)
    ux, uy, uz = H

    R = np.array([(cos + (ux ** 2) * (1 - cos), ux * uy * (1 - cos) - uz * sin, ux * uz * (1 - cos) + uy * sin),
                  (uy * ux * (1 - cos) + uz * sin, cos + (uy ** 2) * (1 - cos), uy * uz * (1 - cos) - ux * sin),
                  (uz * ux * (1 - cos) - uy * sin, uz * uy * (1 - cos) + ux * sin, cos + (uz ** 2) * (1 - cos))])
    return R

# 회전
def rotation_pos(rotate_pos, origin_pos, compare_pos, r1, r2=None):
    origin_pos = rotate_pos -origin_pos
    rotation_V = r2 @ r1 @ origin_pos if r2 is not None else r1 @ origin_pos

    return rotation_V + compare_pos


#======= 위에 까지는 필요한 함수 정의, 아래 좌표값 입력및 실행 ========#
origin_pos = np.array([(-0.500000,	0.000000,	2.121320),
                       (0.500000,	0.000000,	2.121320),
                       (0.500000,	-0.707107,	2.828427)])

compare_pos = np.array([(1.363005,	-0.427130,	2.339082),
                        (1.748084,	0.437983,	2.017688),
                        (2.636461,	0.184843,	2.400710)])


# A, A'의 평면의 법선 벡터
origin_H = np.cross((origin_pos[1]-origin_pos[0]),(origin_pos[2]-origin_pos[0]))
compare_H = np.cross((compare_pos[1]-compare_pos[0]), (compare_pos[2]-compare_pos[0]))
#print(f"A의 법선 벡터 : {origin_H}")
#print(f"A'의 법선 벡터 : {compare_H}")

# A가 A'로 변하기 위해 각도 구하기.
theta = roatation_theta(origin_H, compare_H)
#print(f"회전 radian: {theta: .3f}")

# 회전 행렬
r1 = rotation_matrix(origin_H, compare_H)
#print(f"회전행렬 r1: {r1}")

# A의 p1, p3을 A'의 p1', p3'로 변하기 위해 각도 구하기.
r1_p1p3 = r1@(origin_pos[2]-origin_pos[0])
p1p3 = compare_pos[2]-compare_pos[0]

r2 = rotation_matrix(r1_p1p3, p1p3)
#print(f"회전행렬 r2: {r2}")

origin_p4 = np.array((0.500000, 0.707107, 2.828427))
compare_p4 = np.array((1.498100, 0.871000, 2.883700))

#============= hw5의 정답 부분 =============#
# P4가 P4'로 변환된 부분 및 출력
rotation_p4 = rotation_pos(origin_p4, origin_pos[0], compare_pos[0], r1, r2)
print(f"rotation_p4: {rotation_p4}")
print(f"compare_p4: {compare_p4}")

# P5' 좌표 값 출력
origin_p5 = np.array((1.000000, 1.000000, 1.000000))
rotation_p5 = rotation_pos(origin_p5, origin_pos[0], compare_pos[0], r1, r2)
print(f"rotation_p5: {rotation_p5}")
