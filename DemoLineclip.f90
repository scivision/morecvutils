program test

    implicit none
     
    logical test_lineclip, test_loop

    if(test_lineclip())   print *, 'OK lineclip'

    if(test_loop())  print *, 'OK loop_lineclip'

end program

!------------------------

logical function test_loop()

    use lineclip,only : sp,loop_cohensutherland,assert_isclose
    implicit none


    integer, parameter :: Np=2
    integer i
    real(sp) :: length(Np)
    real(sp),parameter :: xmins(Np)=[1.,2.],ymaxs(Np)=[5.,6.],&
                          xmaxs(Np)=[4.,5.],ymins(Np)=[3.,4.]
    real(sp),parameter :: truelength(Np) =[2.40370083,1.20185041]

    real(sp) :: x1,x2,y1,y2
    x1=0.; y1=0.; x2=4.; y2=6. !not a parameter

    
    call loop_cohensutherland(xmins,ymaxs,xmaxs,ymins,Np,x1,y1,x2,y2,length)
    
    
    do concurrent (i=1:Np)
        if (.not.assert_isclose(length(i),truelength(i)))  error stop
    enddo
    
    test_loop=.true.


end function test_loop

!--------------------

logical function test_lineclip()

    use lineclip, only : sp,cohensutherland,assert_isclose
    implicit none

    real(sp) :: x1, y1, x2, y2  !not a parameter
    logical outside

!    make box with corners LL/UR (1,3) (4,5)
!    and line segment with ends (0,0) (4,6)

! LOWER to UPPER test   
    x1=0.; y1=0.; x2=4.; y2=6.

    call cohensutherland(1., 5., 4., 3.,x1,y1,x2,y2,outside)
    
    if (.not.assert_isclose(x1,2.)) error stop 'tolerance fail x1'
    if (.not.assert_isclose(y1,3.)) error stop 'tolerance fail y1'
    if (.not.assert_isclose(x2,3.3333333)) error stop 'tolerance fail x2'
    if (.not.assert_isclose(y2,5.)) error stop 'tolerance fail y2'

    test_lineclip=.true.

end function test_lineclip
