# This file is a template for simple plots
# Ursa Ursic, Apr 2023


def main():
    # Define data to plot
    # I am plotting 1D array of x values and 1D array of y values (with corresponding indices)
    x1, y1 = simple_exp_plot_data(N=100, k=30, noise=0.08)
    x2, y2 = simple_exp_plot_data(N=100, k=50, noise=0.05)
    x3, y3 = simple_exp_plot_data(N=100, k=60, noise=0.06)

    a1, b1 = simple_sin_plot(N=50, omega=0.3, noise=0.2)
    # 1D array of error values for a1
    a1_err = 4*simple_histogram_data(50)
    # 1D array of error values for b1
    b1_err = 0.1*simple_histogram_data(50)

    # Define figure: in tis case it consists of 2 subplots next to eachother
    fig, ax = plt.subplots(1, 2, sharex=False, sharey=False)

    # Default figsize is set in .mplstyle document, but it can be changed with the following two commands:
    fig.set_figheight(4)
    fig.set_figwidth(10)

    # Main title
    #fig.suptitle("Making figures is fun", fontsize=16)

    # Since we defined a figure with two subplots, ax is a list of two elements
    # Here we plot everything on the left plot
    ax[0].set_title('Subplot a')
    ax[0].plot(x1, y1, label='line 1')
    ax[0].plot(x2, y2, label='line 2')
    ax[0].plot(x3, y3, label='line 3')
    ax[0].plot(x1, 2*y1, label='line 1')
    ax[0].plot(x2, 1.5*y2, label='line 2')
    ax[0].plot(x3, 1.8*y3, label='line 3')
    ax[0].legend(loc="upper right")
    ax[0].set_xlabel('x axis ')
    ax[0].set_ylabel('y axis [units]')
    # get rid of top and right border of the plot
    ax[0].spines[['top', 'right']].set_visible(False)

    # Here we plot everything on the right pot
    ax[1].set_title('Subplot b')
    ax[1].errorbar(a1, b1, xerr=a1_err, yerr=b1_err,
                   ecolor="#515151", elinewidth=1, barsabove=True)
    # ax[1].legend(loc="upper right")
    ax[1].set_xlabel('x axis [units]')
    ax[1].set_ylabel('y axis [units]')
    # get rid of top and right border of the plot
    ax[1].spines[['top', 'right']].set_visible(False)
    plt.show()
    # plt.savefig("fig1.png", dpi=300)        # save the figure with a high resolution

    # Another exaple with just one plot on the figure
    plt.style.use(style)
    fig = plt.figure()

    plt.title("Title")
    plt.fill_between(x1, y1, 1.8*y1, alpha=0.3, zorder=1)
    plt.plot(x1, 1.4*y1, zorder=2, label='curve 1')
    plt.fill_between(x2, y2, 2*y2, alpha=0.3, zorder=3)
    plt.plot(x2, 1.5*y2, zorder=4, label='curve 2')
    plt.fill_between(x3, y3, 1.4*y3, alpha=0.3, zorder=5)
    plt.plot(x3, 1.2*y3, zorder=6, label='curve 3')
    plt.xlabel('x [units]')
    plt.ylabel('y [units]')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
