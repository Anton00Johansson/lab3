""" 
Gives the x-distance from this players cannon to a projectile. 
If the cannon and the projectile touch 
(assuming the projectile is on the ground and factoring in both cannon and projectile size) 
this method should return 0
"""
def projectileDistance(self, proj):
    playerPos = Player.getX(self)
    projectilePos = Projectile.getX(proj)
    compBallSize = self.game.getBallSize()
    compCannonSize = self.game.getCannonSize()
    
    if projectilePos >= (playerPos - compCannonSize/2) and projectilePos <= (playerPos + compCannonSize/2): # If projectile lands on cannon 
        distance = 0
    elif projectilePos > playerPos:                                            
    # If projectile lands one the right side of the cannon
        distance = projectilePos - playerPos - (compCannonSize/2) - compBallSize
    elif projectilePos < playerPos:                                            
    # If the projectile lands on the left side of the cannon 
        distance = - playerPos + projectilePos + (compCannonSize/2) + compBallSize
    return distance 