#include <stdio.h>

void max_souvenirs()
{
    int machine[3][4];
    int max_souvenir_count = 0;
    int best_combination[3] = {0, 0, 0};

    // Get machine constraints from the user
    printf("Enter machine constraints (3 machines, each with 4 values - minutes):\n");
    for (int i = 0; i < 3; i++)
    {
        printf("Machine %d: ", i + 1);
        scanf("%d %d %d %d", &machine[i][0], &machine[i][1], &machine[i][2], &machine[i][3]);
    }

    for (int x = 1; x <= machine[0][3]; x++)
    { // maximum possible value of x based on constraint 1
        for (int y = 1; y <= machine[1][3]; y++)
        { // maximum possible value of y based on constraint 2
            for (int z = 1; z <= machine[2][3]; z++)
            { // maximum possible value of z based on constraint 3
                if ((machine[0][0] * x + machine[0][1] * y + machine[0][2] * z <= machine[0][3]) &&
                    (machine[1][0] * x + machine[1][1] * y + machine[1][2] * z <= machine[1][3]) &&
                    (machine[2][0] * x + machine[2][1] * y + machine[2][2] * z <= machine[2][3]))
                {
                    int total_souvenirs = x + y + z;
                    if (total_souvenirs > max_souvenir_count)
                    {
                        max_souvenir_count = total_souvenirs;
                        best_combination[0] = x;
                        best_combination[1] = y;
                        best_combination[2] = z;
                    }
                }
            }
        }
    }

    printf("Maximum number of souvenirs: %d\n", max_souvenir_count);
    printf("Number of Type A souvenirs: %d\n", best_combination[0]);
    printf("Number of Type B souvenirs: %d\n", best_combination[1]);
    printf("Number of Type C souvenirs: %d\n", best_combination[2]);
}

int main()
{
    max_souvenirs();
    return 0;
}
