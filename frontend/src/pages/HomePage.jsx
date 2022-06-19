import React from 'react';
import { useState } from 'react';
import { Button, Grid, MenuItem, Select, TextField } from "@mui/material"

export const HomePage = () => {
    const [mounted,setMounted] = useState(false);

    return (
        <div>
            <Grid>
                <Grid item textAlign={true}>
                    The Girth
                </Grid>
                <Grid item>
                    <Button>
                        Wordle Solver
                    </Button>
                </Grid>
                <Grid item>
                    <Button>
                        Tester
                    </Button>
                </Grid>
                <Grid item>
                    <Button>
                        About
                    </Button>
                </Grid>
            </Grid>
        </div>
    )
}