import numpy as np

def euler2quat(roll_deg, pitch_deg, yaw_deg):
    """Convert Euler angles (degrees) to quaternion [w, x, y, z]."""
    roll = np.deg2rad(roll_deg)
    pitch = np.deg2rad(pitch_deg)
    yaw = np.deg2rad(yaw_deg)

    cr = np.cos(roll/2)
    cp = np.cos(pitch/2)
    cy = np.cos(yaw/2)

    sr = np.sin(roll/2)
    sp = np.sin(pitch/2)
    sy = np.sin(yaw/2)

    w = cr*cp*cy + sr*sp*sy
    x = sr*cp*cy - cr*sp*sy
    y = cr*sp*cy + sr*cp*sy
    z = cr*cp*sy - sr*sp*cy

    return [w, x, y, z]

def quat2euler(w,x,y,z, degrees=True):
    """Convert quaternion [w, x, y, z] to Euler angles (roll, pitch, yaw)."""
    
    # Normalize quaternion
    norm = np.sqrt(w*w + x*x + y*y + z*z)
    w, x, y, z = w/norm, x/norm, y/norm, z/norm

    # Roll (X-axis rotation)
    sinr_cosp = 2*(w*x + y*z)
    cosr_cosp = 1 - 2*(x*x + y*y)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    # Pitch (Y-axis rotation)
    sinp = 2*(w*y - z*x)
    if abs(sinp) >= 1:
        pitch = np.sign(sinp) * (np.pi/2)  # Gimbal lock
    else:
        pitch = np.arcsin(sinp)

    # Yaw (Z-axis rotation)
    siny_cosp = 2*(w*z + x*y)
    cosy_cosp = 1 - 2*(y*y + z*z)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

    if degrees:
        roll, pitch, yaw = np.degrees([roll, pitch, yaw])

    return [roll, pitch, yaw]


req=int(input("Euler angles (degrees) ---> quaternion | Press 1, \nquaternion [w, x, y, z] --> Euler angles | Press 2: "  ))

if req == 1:
    roll_deg= float(input("Enter the roll angle: "))
    pitch_deg= float(input("Enter the pitch angle: "))
    yaw_deg= float(input("Enter the yaw angle: "))
    ans=euler2quat(roll_deg, pitch_deg, yaw_deg)
    print(ans)
    
elif req==2:
    w= float(input("w: "))
    x= float(input("x: "))
    y= float(input("y: "))
    z= float(input("z: "))
    ans=quat2euler(w,x,y,z)
    print(ans)
    
else:
    print("Invalid input!")
