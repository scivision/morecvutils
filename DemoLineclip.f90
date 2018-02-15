program test

    use lineclip,only:wp, loop_cohensutherland, cohensutherland
    use assert

    implicit none

    call test_lineclip()

    call test_loop()

contains
  
subroutine test_loop()

    integer, parameter :: Np=2
    real(wp) :: length(Np)
    real(wp),parameter :: xmins(Np)=[1.,2.],ymaxs(Np)=[5.,6.],&
                          xmaxs(Np)=[4.,5.],ymins(Np)=[3.,4.]
    real(wp),parameter :: truelength(Np) =[2.40370083,1.20185041]

    real(wp) :: x1,x2,y1,y2
    x1=0.; y1=0.; x2=4.; y2=6. !not a parameter

    
    call loop_cohensutherland(xmins,ymaxs,xmaxs,ymins,Np,x1,y1,x2,y2,length)
    
    
    call assert_isclose(length, truelength)
    
    print *, 'OK loop_lineclip'
    

end subroutine test_loop

!--------------------

subroutine test_lineclip()

    real(wp) :: x1, y1, x2, y2  !not a parameter

!    make box with corners LL/UR (1,3) (4,5)
!    and line segment with ends (0,0) (4,6)

! LOWER to UPPER test   
    x1=0.; y1=0.; x2=4.; y2=6.

    call cohensutherland(1._wp, 5._wp, 4._wp, 3._wp,x1,y1,x2,y2)
    
    call assert_isclose(x1, 2._wp)
    call assert_isclose(y1, 3._wp)
    call assert_isclose(x2, 3.3333333_wp)
    call assert_isclose(y2, 5._wp)
    
    print *, 'OK lineclip'
    
end subroutine test_lineclip

end program
